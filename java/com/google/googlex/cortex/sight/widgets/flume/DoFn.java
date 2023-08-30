/*
 * Copyright 2023 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.googlex.cortex.sight.widgets.flume;

import com.google.analysis.dremel.core.capacitor.CapacitorException;
import com.google.common.base.Pair;
import com.google.common.flogger.GoogleLogger;
import com.google.googlex.cortex.sight.Location;
import com.google.googlex.cortex.sight.Sight;
import com.google.googlex.cortex.sight.SightImpl;
import com.google.pipeline.flume.fj.FJ;
import com.google.protos.sight.x.proto.Sight.Params;
import java.io.IOException;
import org.checkerframework.checker.nullness.qual.Nullable;

/** Wraps Flume DoFn class with a Sight loggable variant. */
public abstract class DoFn<I, O> extends FJ.DoFn<Pair<SightId, I>, Pair<SightId, O>> {
  private static final GoogleLogger logger = GoogleLogger.forEnclosingClass();

  public abstract void process(I elem, EmitFn<O> emitFn, Sight sight);

  @Override
  public void process(Pair<SightId, I> input, FJ.EmitFn<Pair<SightId, O>> baseEmitFn) {
    try (DoFnProcessBlock block =
        DoFnProcessBlock.create(derivedClassName, input.getFirst(), sight)) {
      if (emitFn == null) {
        emitFn = EmitFn.create(/* stageId= */ System.identityHashCode(this), baseEmitFn, sight);
      }
      process(input.getSecond(), emitFn, sight);
    }
  }

  private final Params params;

  private String derivedClassName;

  private @Nullable SightImpl sight;

  private @Nullable EmitFn<O> emitFn;

  protected DoFn(Sight baseSight, String derivedClassName) {
    synchronized (baseSight) {
      Location location = DoFnUtils.emitDoFnCreate(derivedClassName, baseSight);

      params =
          baseSight.getParams().toBuilder()
              .setLocal(true)
              .setContainerLocation(location.toString())
              .build();
      this.derivedClassName = derivedClassName;
      sight = null;
      emitFn = null;

      DoFnUtils.emitDoFnComplete(derivedClassName, baseSight);
    }
  }

  protected DoFn(Params params) {
    this.params = params;
  }

  @Override
  public void initialize() {
    try {
      sight = SightImpl.create(params);
    } catch (CapacitorException | IOException e) {
      logger.atSevere().withCause(e).log("While creating SightImpl");
    }
    sight.getLocation().enter(sight.hashCode());
    sight.setAttribute("FlumeStageClass", derivedClassName);
  }

  @Override
  public void terminate() {
    sight.unsetAttribute("FlumeStageClass");
    sight.getLocation().exit();
    sight.close();
  }
}
