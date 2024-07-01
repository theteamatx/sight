# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sight/proto/sight.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sight.proto import example_pb2 as sight_dot_proto_dot_example__pb2
from sight.proto.widgets.pipeline.flume import flume_pb2 as sight_dot_proto_dot_widgets_dot_pipeline_dot_flume_dot_flume__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17sight/proto/sight.proto\x12\rsight.x.proto\x1a\x19sight/proto/example.proto\x1a.sight/proto/widgets/pipeline/flume/flume.proto\"\'\n\tAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xb1\x0c\n\x06Object\x12\x10\n\x08location\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x03\x12\x0f\n\x07log_uid\x18\x18 \x01(\t\x12+\n\tattribute\x18\x03 \x03(\x0b\x32\x18.sight.x.proto.Attribute\x12/\n\x08sub_type\x18\x04 \x01(\x0e\x32\x1d.sight.x.proto.Object.SubType\x12#\n\x04text\x18\x05 \x01(\x0b\x32\x13.sight.x.proto.TextH\x00\x12\x30\n\x0b\x62lock_start\x18\x06 \x01(\x0b\x32\x19.sight.x.proto.BlockStartH\x00\x12,\n\tblock_end\x18\x07 \x01(\x0b\x32\x17.sight.x.proto.BlockEndH\x00\x12\x38\n\x0f\x61ttribute_start\x18\x08 \x01(\x0b\x32\x1d.sight.x.proto.AttributeStartH\x00\x12\x34\n\rattribute_end\x18\t \x01(\x0b\x32\x1b.sight.x.proto.AttributeEndH\x00\x12\x46\n\x10\x66lume_do_fn_emit\x18\x0e \x01(\x0b\x32*.sight.x.widgets.flume.proto.FlumeDoFnEmitH\x00\x12@\n\x0c\x66lume_depend\x18\x0f \x01(\x0b\x32(.sight.x.widgets.flume.proto.FlumeDependH\x00\x12%\n\x05value\x18\x10 \x01(\x0b\x32\x14.sight.x.proto.ValueH\x00\x12-\n\texception\x18\x11 \x01(\x0b\x32\x18.sight.x.proto.ExceptionH\x00\x12\'\n\x06tensor\x18\x14 \x01(\x0b\x32\x15.sight.x.proto.TensorH\x00\x12?\n\x13tensor_flow_example\x18\x15 \x01(\x0b\x32 .sight.x.proto.TensorFlowExampleH\x00\x12\x36\n\x0e\x64\x65\x63ision_point\x18\x16 \x01(\x0b\x32\x1c.sight.x.proto.DecisionPointH\x00\x12:\n\x10\x64\x65\x63ision_outcome\x18\x17 \x01(\x0b\x32\x1e.sight.x.proto.DecisionOutcomeH\x00\x12#\n\x04link\x18\x19 \x01(\x0b\x32\x13.sight.x.proto.LinkH\x00\x12\x36\n\x0epropose_action\x18\x1a \x01(\x0b\x32\x1c.sight.x.proto.ProposeActionH\x00\x12\x0c\n\x04\x66ile\x18\n \x01(\t\x12\x0c\n\x04line\x18\x0b \x01(\x05\x12\x0c\n\x04\x66unc\x18\x0c \x01(\t\x12\x1f\n\x17\x61ncestor_start_location\x18\r \x03(\t\x12.\n\x07metrics\x18\x12 \x01(\x0b\x32\x1d.sight.x.proto.Object.Metrics\x12*\n\x05order\x18\x13 \x01(\x0b\x32\x1b.sight.x.proto.Object.Order\x1aX\n\x07Metrics\x12%\n\x1dprocess_free_swap_space_bytes\x18\x01 \x01(\x03\x12&\n\x1eprocess_total_swap_space_bytes\x18\x02 \x01(\x03\x1a\x1d\n\x05Order\x12\x14\n\x0ctimestamp_ns\x18\x01 \x01(\x03\"\xd2\x02\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x0b\n\x07ST_TEXT\x10\x01\x12\x12\n\x0eST_BLOCK_START\x10\x02\x12\x10\n\x0cST_BLOCK_END\x10\x03\x12\x16\n\x12ST_ATTRIBUTE_START\x10\x04\x12\x14\n\x10ST_ATTRIBUTE_END\x10\x05\x12\x17\n\x13ST_FLUME_DO_FN_EMIT\x10\x06\x12\x13\n\x0fST_FLUME_DEPEND\x10\x07\x12\x0c\n\x08ST_VALUE\x10\x08\x12\x10\n\x0cST_EXCEPTION\x10\t\x12\r\n\tST_TENSOR\x10\n\x12\x19\n\x15ST_TENSORFLOW_EXAMPLE\x10\x0c\x12\x15\n\x11ST_DECISION_POINT\x10\r\x12\x17\n\x13ST_DECISION_OUTCOME\x10\x0e\x12\n\n\x06ST_GAP\x10\x0b\x12\x0b\n\x07ST_LINK\x10\x0f\x12\x15\n\x11ST_PROPOSE_ACTION\x10\x10\x42\x12\n\x10sub_type_message\"\x88\x01\n\rProposeAction\x12\x32\n\x0c\x61\x63tion_attrs\x18\x01 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x30\n\nattributes\x18\x02 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x11\n\taction_id\x18\x03 \x01(\t\"\xec\x01\n\x12\x43onfigurationStart\x12;\n\x08sub_type\x18\x01 \x01(\x0e\x32).sight.x.proto.ConfigurationStart.SubType\x12K\n\x16\x64\x65\x63ision_configuration\x18\x02 \x01(\x0b\x32).sight.x.proto.DecisionConfigurationStartH\x00\"8\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x1d\n\x19ST_DECISION_CONFIGURATION\x10\x01\x42\x12\n\x10sub_type_message\";\n\tException\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\ttraceback\x18\x03 \x01(\t\"\xd7\x05\n\x06Tensor\x12/\n\x08sub_type\x18\x01 \x01(\x0e\x32\x1d.sight.x.proto.Tensor.SubType\x12\r\n\x05label\x18\x02 \x01(\t\x12\r\n\x05shape\x18\x03 \x03(\x03\x12\x11\n\tdim_label\x18\t \x03(\t\x12;\n\x0f\x64im_axis_values\x18\n \x03(\x0b\x32\".sight.x.proto.Tensor.StringValues\x12;\n\rstring_values\x18\x04 \x01(\x0b\x32\".sight.x.proto.Tensor.StringValuesH\x00\x12\x39\n\x0c\x62ytes_values\x18\x05 \x01(\x0b\x32!.sight.x.proto.Tensor.BytesValuesH\x00\x12\x39\n\x0cint64_values\x18\x06 \x01(\x0b\x32!.sight.x.proto.Tensor.Int64ValuesH\x00\x12;\n\rdouble_values\x18\x07 \x01(\x0b\x32\".sight.x.proto.Tensor.DoubleValuesH\x00\x12\x37\n\x0b\x62ool_values\x18\x08 \x01(\x0b\x32 .sight.x.proto.Tensor.BoolValuesH\x00\x1a\x1d\n\x0cStringValues\x12\r\n\x05value\x18\x01 \x03(\t\x1a\x1c\n\x0b\x42ytesValues\x12\r\n\x05value\x18\x01 \x03(\x0c\x1a\x1c\n\x0bInt64Values\x12\r\n\x05value\x18\x01 \x03(\x03\x1a\x1d\n\x0c\x44oubleValues\x12\r\n\x05value\x18\x01 \x03(\x01\x1a\x1b\n\nBoolValues\x12\r\n\x05value\x18\x01 \x03(\x08\"`\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\r\n\tST_STRING\x10\x01\x12\x0c\n\x08ST_BYTES\x10\x02\x12\x0c\n\x08ST_INT64\x10\x03\x12\r\n\tST_DOUBLE\x10\x04\x12\x0b\n\x07ST_BOOL\x10\x05\x42\x0c\n\nvalue_type\"\x9c\x01\n\x04Link\x12\x17\n\x0flinked_sight_id\x18\x01 \x01(\t\x12/\n\tlink_type\x18\x02 \x01(\x0e\x32\x1c.sight.x.proto.Link.LinkType\"J\n\x08LinkType\x12\x0e\n\nLT_UNKNOWN\x10\x00\x12\x16\n\x12LT_PARENT_TO_CHILD\x10\x01\x12\x16\n\x12LT_CHILD_TO_PARENT\x10\x02\"\x8e\x02\n\x11TensorFlowExample\x12/\n\rinput_example\x18\x01 \x01(\x0b\x32\x16.sight.x.proto.ExampleH\x00\x12@\n\x16input_sequence_example\x18\x02 \x01(\x0b\x32\x1e.sight.x.proto.SequenceExampleH\x00\x12\x30\n\x0eoutput_example\x18\x03 \x01(\x0b\x32\x16.sight.x.proto.ExampleH\x01\x12\x41\n\x17output_sequence_example\x18\x04 \x01(\x0b\x32\x1e.sight.x.proto.SequenceExampleH\x01\x42\x07\n\x05inputB\x08\n\x06output\")\n\x03Log\x12\"\n\x03obj\x18\x01 \x03(\x0b\x32\x15.sight.x.proto.Object\"x\n\x04Text\x12\x0c\n\x04text\x18\x01 \x01(\t\x12-\n\x08sub_type\x18\x02 \x01(\x0e\x32\x1b.sight.x.proto.Text.SubType\"3\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x0b\n\x07ST_TEXT\x10\x01\x12\x0b\n\x07ST_HTML\x10\x02\"\xbe\x02\n\x05Value\x12.\n\x08sub_type\x18\x01 \x01(\x0e\x32\x1c.sight.x.proto.Value.SubType\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x03 \x01(\x0cH\x00\x12\x15\n\x0bint64_value\x18\x04 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00\x12\x14\n\nbool_value\x18\x06 \x01(\x08H\x00\x12\x14\n\nnone_value\x18\x07 \x01(\x08H\x00\"m\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\r\n\tST_STRING\x10\x01\x12\x0c\n\x08ST_BYTES\x10\x02\x12\x0c\n\x08ST_INT64\x10\x03\x12\r\n\tST_DOUBLE\x10\x04\x12\x0b\n\x07ST_BOOL\x10\x05\x12\x0b\n\x07ST_NONE\x10\x06\x42\x0c\n\nvalue_type\"\xa8\n\n\nBlockStart\x12\r\n\x05label\x18\x01 \x01(\t\x12\x33\n\x08sub_type\x18\x02 \x01(\x0e\x32!.sight.x.proto.BlockStart.SubType\x12J\n\x12\x66lume_do_fn_create\x18\x03 \x01(\x0b\x32,.sight.x.widgets.flume.proto.FlumeDoFnCreateH\x00\x12M\n\x14\x66lume_do_fn_start_do\x18\x04 \x01(\x0b\x32-.sight.x.widgets.flume.proto.FlumeDoFnStartDoH\x00\x12T\n\x17\x66lume_compare_fn_create\x18\x05 \x01(\x0b\x32\x31.sight.x.widgets.flume.proto.FlumeCompareFnCreateH\x00\x12\x61\n\x1e\x66lume_compare_fn_start_compare\x18\x06 \x01(\x0b\x32\x37.sight.x.widgets.flume.proto.FlumeCompareFnStartCompareH\x00\x12(\n\x04list\x18\x07 \x01(\x0b\x32\x18.sight.x.proto.ListStartH\x00\x12\\\n tensor_flow_model_training_epoch\x18\x08 \x01(\x0b\x32\x30.sight.x.proto.TensorFlowModelTrainingEpochStartH\x00\x12:\n\x10simulation_start\x18\t \x01(\x0b\x32\x1e.sight.x.proto.SimulationStartH\x00\x12O\n\x1bsimulation_parameters_start\x18\n \x01(\x0b\x32(.sight.x.proto.SimulationParametersStartH\x00\x12L\n\x1asimulation_time_step_start\x18\x0b \x01(\x0b\x32&.sight.x.proto.SimulationTimeStepStartH\x00\x12:\n\rconfiguration\x18\x0c \x01(\x0b\x32!.sight.x.proto.ConfigurationStartH\x00\"\xce\x03\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x19\n\x15ST_FLUME_DO_FN_CREATE\x10\x01\x12\x1b\n\x17ST_FLUME_DO_FN_START_DO\x10\x02\x12\x1e\n\x1aST_FLUME_COMPARE_FN_CREATE\x10\x03\x12%\n!ST_FLUME_COMPARE_FN_START_COMPARE\x10\x04\x12\x12\n\x0eST_NAMED_VALUE\x10\x05\x12\x0b\n\x07ST_LIST\x10\x06\x12\x0c\n\x08ST_TABLE\x10\x07\x12#\n\x1fST_TENSORFLOW_MODEL_APPLICATION\x10\x08\x12&\n\"ST_TENSORFLOW_MODEL_TRAINING_EPOCH\x10\t\x12 \n\x1cST_TENSORFLOW_MODEL_TRAINING\x10\n\x12\x11\n\rST_SIMULATION\x10\x0b\x12\x1c\n\x18ST_SIMULATION_PARAMETERS\x10\x0c\x12\x17\n\x13ST_SIMULATION_STATE\x10\r\x12\x1b\n\x17ST_SIMULATION_TIME_STEP\x10\x0e\x12\x19\n\x15ST_CLUSTER_ASSIGNMENT\x10\x0f\x12\x14\n\x10ST_CONFIGURATION\x10\x10\x42\x12\n\x10sub_type_message\"\xa4\x08\n\x08\x42lockEnd\x12\r\n\x05label\x18\x01 \x01(\t\x12\x31\n\x08sub_type\x18\x06 \x01(\x0e\x32\x1f.sight.x.proto.BlockEnd.SubType\x12\x1f\n\x17location_of_block_start\x18\x02 \x01(\t\x12\x1b\n\x13num_direct_contents\x18\x03 \x01(\x03\x12\x1f\n\x17num_transitive_contents\x18\x04 \x01(\x03\x12N\n\x14\x66lume_do_fn_complete\x18\x07 \x01(\x0b\x32..sight.x.widgets.flume.proto.FlumeDoFnCompleteH\x00\x12I\n\x12\x66lume_do_fn_end_do\x18\x08 \x01(\x0b\x32+.sight.x.widgets.flume.proto.FlumeDoFnEndDoH\x00\x12X\n\x19\x66lume_compare_fn_complete\x18\t \x01(\x0b\x32\x33.sight.x.widgets.flume.proto.FlumeCompareFnCompleteH\x00\x12]\n\x1c\x66lume_compare_fn_end_compare\x18\n \x01(\x0b\x32\x35.sight.x.widgets.flume.proto.FlumeCompareFnEndCompareH\x00\x12\x30\n\x07metrics\x18\x0c \x01(\x0b\x32\x1f.sight.x.proto.BlockEnd.Metrics\x1a\"\n\x07Metrics\x12\x17\n\x0f\x65lapsed_time_ns\x18\x01 \x01(\x03\"\xb8\x03\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x1b\n\x17ST_FLUME_DO_FN_COMPLETE\x10\x01\x12\x19\n\x15ST_FLUME_DO_FN_END_DO\x10\x02\x12 \n\x1cST_FLUME_COMPARE_FN_COMPLETE\x10\x03\x12#\n\x1fST_FLUME_COMPARE_FN_END_COMPARE\x10\x04\x12\x12\n\x0eST_NAMED_VALUE\x10\x05\x12\x0b\n\x07ST_LIST\x10\x06\x12\x0c\n\x08ST_TABLE\x10\x07\x12#\n\x1fST_TENSORFLOW_MODEL_APPLICATION\x10\x08\x12&\n\"ST_TENSORFLOW_MODEL_TRAINING_EPOCH\x10\t\x12 \n\x1cST_TENSORFLOW_MODEL_TRAINING\x10\n\x12\x11\n\rST_SIMULATION\x10\x0b\x12\x1c\n\x18ST_SIMULATION_PARAMETERS\x10\x0c\x12\x17\n\x13ST_SIMULATION_STATE\x10\r\x12\x1b\n\x17ST_SIMULATION_TIME_STEP\x10\x0e\x12\x19\n\x15ST_CLUSTER_ASSIGNMENT\x10\x0f\x42\x12\n\x10sub_type_message\"\xaf\x01\n\tListStart\x12\x32\n\x08sub_type\x18\x01 \x01(\x0e\x32 .sight.x.proto.ListStart.SubType\"n\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x12\n\x0eST_HOMOGENEOUS\x10\x01\x12\x14\n\x10ST_HETEROGENEOUS\x10\x02\x12\n\n\x06ST_MAP\x10\x03\x12\x10\n\x0cST_MAP_ENTRY\x10\x04\x12\x0b\n\x07ST_DICT\x10\x05\"J\n!TensorFlowModelTrainingEpochStart\x12\x11\n\tepoch_num\x18\x01 \x01(\x03\x12\x12\n\nbatch_size\x18\x02 \x01(\x03\"=\n\x0e\x41ttributeStart\x12+\n\tattribute\x18\x01 \x01(\x0b\x32\x18.sight.x.proto.Attribute\"\x1b\n\x0c\x41ttributeEnd\x12\x0b\n\x03key\x18\x01 \x01(\t\"\xb2\x03\n\x06Params\x12\r\n\x05local\x18\x01 \x01(\x08\x12\x14\n\x0clog_dir_path\x18\x02 \x01(\t\x12\r\n\x05label\x18\x03 \x01(\t\x12\x13\n\x0btext_output\x18\x04 \x01(\x08\x12\x17\n\x0f\x63olumnio_output\x18\x05 \x01(\x08\x12\x18\n\x10\x63\x61pacitor_output\x18\x06 \x01(\x08\x12\x11\n\tlog_owner\x18\x07 \x01(\t\x12\x13\n\x0bpath_prefix\x18\x08 \x01(\t\x12\x1a\n\x12\x63ontainer_location\x18\t \x01(\t\x12\n\n\x02id\x18\n \x01(\x03\x12\x15\n\rsilent_logger\x18\x0b \x01(\x08\x12\x11\n\tin_memory\x18\x0c \x01(\x08\x12\x13\n\x0b\x61vro_output\x18\r \x01(\x08\x12\x12\n\nproject_id\x18\x0e \x01(\t\x12\x13\n\x0b\x62ucket_name\x18\x0f \x01(\t\x12\x10\n\x08gcp_path\x18\x10 \x01(\t\x12\x13\n\x0b\x66ile_format\x18\x11 \x01(\t\x12\x14\n\x0c\x64\x61taset_name\x18\x12 \x01(\t\x12\x1c\n\x14\x65xternal_file_format\x18\x13 \x01(\t\x12\x19\n\x11\x65xternal_file_uri\x18\x14 \x01(\t\"\x11\n\x0fSimulationStart\"\x1b\n\x19SimulationParametersStart\"\xb8\x02\n\x17SimulationTimeStepStart\x12\x17\n\x0ftime_step_index\x18\x01 \x03(\x03\x12\x11\n\ttime_step\x18\x02 \x01(\x02\x12\x16\n\x0etime_step_size\x18\x03 \x01(\x02\x12M\n\x0ftime_step_units\x18\x04 \x01(\x0e\x32\x34.sight.x.proto.SimulationTimeStepStart.TimeStepUnits\"\x89\x01\n\rTimeStepUnits\x12\x0f\n\x0bTSU_UNKNOWN\x10\x00\x12\x0e\n\nTSU_SECOND\x10\x01\x12\x0e\n\nTSU_MINUTE\x10\x02\x12\x0c\n\x08TSU_HOUR\x10\x03\x12\x0b\n\x07TSU_DAY\x10\x04\x12\r\n\tTSU_MONTH\x10\x05\x12\x0f\n\x0bTSU_QUARTER\x10\x06\x12\x0c\n\x08TSU_YEAR\x10\x07\"\xf0\x01\n\x12\x43ontinuousProbDist\x12>\n\x08gaussian\x18\x01 \x01(\x0b\x32*.sight.x.proto.ContinuousProbDist.GaussianH\x00\x12<\n\x07uniform\x18\x02 \x01(\x0b\x32).sight.x.proto.ContinuousProbDist.UniformH\x00\x1a\'\n\x08Gaussian\x12\x0c\n\x04mean\x18\x01 \x01(\x02\x12\r\n\x05stdev\x18\x02 \x01(\x02\x1a+\n\x07Uniform\x12\x0f\n\x07min_val\x18\x01 \x01(\x02\x12\x0f\n\x07max_val\x18\x02 \x01(\x02\x42\x06\n\x04\x64ist\"\x83\x01\n\x10\x44iscreteProbDist\x12:\n\x07uniform\x18\x01 \x01(\x0b\x32\'.sight.x.proto.DiscreteProbDist.UniformH\x00\x1a+\n\x07Uniform\x12\x0f\n\x07min_val\x18\x01 \x01(\x03\x12\x0f\n\x07max_val\x18\x02 \x01(\x03\x42\x06\n\x04\x64ist\"\xa6\x1c\n\x1a\x44\x65\x63isionConfigurationStart\x12O\n\x0eoptimizer_type\x18\x01 \x01(\x0e\x32\x37.sight.x.proto.DecisionConfigurationStart.OptimizerType\x12R\n\rchoice_config\x18\x02 \x03(\x0b\x32;.sight.x.proto.DecisionConfigurationStart.ChoiceConfigEntry\x12N\n\x0bstate_attrs\x18\x03 \x03(\x0b\x32\x39.sight.x.proto.DecisionConfigurationStart.StateAttrsEntry\x12P\n\x0c\x61\x63tion_attrs\x18\x04 \x03(\x0b\x32:.sight.x.proto.DecisionConfigurationStart.ActionAttrsEntry\x12R\n\routcome_attrs\x18\x05 \x03(\x0b\x32;.sight.x.proto.DecisionConfigurationStart.OutcomeAttrsEntry\x12\x12\n\nnum_trials\x18\x06 \x01(\x03\x1a\x0e\n\x0cVizierConfig\x1a\xf1\x01\n\nAcmeConfig\x12R\n\nacme_agent\x18\x01 \x01(\x0e\x32>.sight.x.proto.DecisionConfigurationStart.AcmeConfig.AcmeAgent\"\x8e\x01\n\tAcmeAgent\x12\x0e\n\nAA_UNKNOWN\x10\x00\x12\n\n\x06\x41\x41_DQN\x10\x01\x12\x0b\n\x07\x41\x41_D4PG\x10\x02\x12\r\n\tAA_IMPALA\x10\x03\x12\x0b\n\x07\x41\x41_MDQN\x10\x04\x12\x0c\n\x08\x41\x41_QRDQN\x10\x05\x12\n\n\x06\x41\x41_PPO\x10\x06\x12\n\n\x06\x41\x41_MPO\x10\x07\x12\n\n\x06\x41\x41_SAC\x10\x08\x12\n\n\x06\x41\x41_TD3\x10\t\x1a\x35\n\x16GeneticAlgorithmConfig\x12\x1b\n\x13max_population_size\x18\x01 \x01(\x03\x1a\x18\n\x16\x45xhaustiveSearchConfig\x1a\xeb\x02\n\tLLMConfig\x12S\n\talgorithm\x18\x01 \x01(\x0e\x32@.sight.x.proto.DecisionConfigurationStart.LLMConfig.LLMAlgorithm\x12I\n\x04goal\x18\x02 \x01(\x0e\x32;.sight.x.proto.DecisionConfigurationStart.LLMConfig.LLMGoal\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"W\n\x0cLLMAlgorithm\x12\x0e\n\nLA_UNKNOWN\x10\x00\x12\x11\n\rLA_TEXT_BISON\x10\x01\x12\x11\n\rLA_CHAT_BISON\x10\x02\x12\x11\n\rLA_GEMINI_PRO\x10\x03\"P\n\x07LLMGoal\x12\x0e\n\nLM_UNKNOWN\x10\x00\x12\x0f\n\x0bLM_OPTIMIZE\x10\x01\x12\x10\n\x0cLM_RECOMMEND\x10\x02\x12\x12\n\x0eLM_INTERACTIVE\x10\x03\x1a\x13\n\x11\x42\x61yesianOptConfig\x1a\x1b\n\x19SensitivityAnalysisConfig\x1a\x8e\x03\n\x0fNeverGradConfig\x12_\n\talgorithm\x18\x01 \x01(\x0e\x32L.sight.x.proto.DecisionConfigurationStart.NeverGradConfig.NeverGradAlgorithm\"\x99\x02\n\x12NeverGradAlgorithm\x12\x0e\n\nNG_UNKNOWN\x10\x00\x12\x0b\n\x07NG_AUTO\x10\x01\x12\t\n\x05NG_BO\x10\x02\x12\n\n\x06NG_CMA\x10\x03\x12\x12\n\x0eNG_TwoPointsDE\x10\x04\x12\x13\n\x0fNG_RandomSearch\x10\x05\x12\n\n\x06NG_PSO\x10\x06\x12\x1a\n\x16NG_ScrHammersleySearch\x10\x07\x12\t\n\x05NG_DE\x10\x08\x12\n\n\x06NG_CGA\x10\t\x12\t\n\x05NG_ES\x10\n\x12\r\n\tNG_DL_OPO\x10\x0b\x12\n\n\x06NG_DDE\x10\x0c\x12\n\n\x06NG_NMM\x10\r\x12\x10\n\x0cNG_TINY_SPSA\x10\x0e\x12\x11\n\rNG_VORONOI_DE\x10\x0f\x12\x10\n\x0cNG_CMA_SMALL\x10\x10\x1a\r\n\x0bSMCPyConfig\x1a\x19\n\x17WorklistSchedulerConfig\x1a\xac\x07\n\x0c\x43hoiceConfig\x12O\n\rvizier_config\x18\x01 \x01(\x0b\x32\x36.sight.x.proto.DecisionConfigurationStart.VizierConfigH\x00\x12K\n\x0b\x61\x63me_config\x18\x02 \x01(\x0b\x32\x34.sight.x.proto.DecisionConfigurationStart.AcmeConfigH\x00\x12\x64\n\x18genetic_algorithm_config\x18\x03 \x01(\x0b\x32@.sight.x.proto.DecisionConfigurationStart.GeneticAlgorithmConfigH\x00\x12\x64\n\x18\x65xhaustive_search_config\x18\x04 \x01(\x0b\x32@.sight.x.proto.DecisionConfigurationStart.ExhaustiveSearchConfigH\x00\x12I\n\nllm_config\x18\x05 \x01(\x0b\x32\x33.sight.x.proto.DecisionConfigurationStart.LLMConfigH\x00\x12Z\n\x13\x62\x61yesian_opt_config\x18\x06 \x01(\x0b\x32;.sight.x.proto.DecisionConfigurationStart.BayesianOptConfigH\x00\x12j\n\x1bsensitivity_analysis_config\x18\x07 \x01(\x0b\x32\x43.sight.x.proto.DecisionConfigurationStart.SensitivityAnalysisConfigH\x00\x12V\n\x11never_grad_config\x18\x08 \x01(\x0b\x32\x39.sight.x.proto.DecisionConfigurationStart.NeverGradConfigH\x00\x12N\n\rsmc_py_config\x18\t \x01(\x0b\x32\x35.sight.x.proto.DecisionConfigurationStart.SMCPyConfigH\x00\x12\x66\n\x19worklist_scheduler_config\x18\n \x01(\x0b\x32\x41.sight.x.proto.DecisionConfigurationStart.WorklistSchedulerConfigH\x00\x42\x0f\n\rchoice_config\x1ak\n\x11\x43hoiceConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.sight.x.proto.DecisionConfigurationStart.ChoiceConfig:\x02\x38\x01\x1a\x8d\x02\n\tAttrProps\x12\x11\n\tmin_value\x18\x01 \x01(\x02\x12\x11\n\tmax_value\x18\x02 \x01(\x02\x12\x11\n\tstep_size\x18\x03 \x01(\x02\x12\x1a\n\x12valid_float_values\x18\x04 \x03(\x02\x12\x18\n\x10valid_int_values\x18\x08 \x03(\x03\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12?\n\x14\x63ontinuous_prob_dist\x18\x06 \x01(\x0b\x32!.sight.x.proto.ContinuousProbDist\x12;\n\x12\x64iscrete_prob_dist\x18\x07 \x01(\x0b\x32\x1f.sight.x.proto.DiscreteProbDist\x1a\x66\n\x0fStateAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32\x33.sight.x.proto.DecisionConfigurationStart.AttrProps:\x02\x38\x01\x1ag\n\x10\x41\x63tionAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32\x33.sight.x.proto.DecisionConfigurationStart.AttrProps:\x02\x38\x01\x1ah\n\x11OutcomeAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32\x33.sight.x.proto.DecisionConfigurationStart.AttrProps:\x02\x38\x01\"\xea\x01\n\rOptimizerType\x12\x0e\n\nOT_UNKNOWN\x10\x00\x12\r\n\tOT_VIZIER\x10\x01\x12\x0b\n\x07OT_ACME\x10\x02\x12\x18\n\x14OT_GENETIC_ALGORITHM\x10\x03\x12\x18\n\x14OT_EXHAUSTIVE_SEARCH\x10\x04\x12\n\n\x06OT_LLM\x10\x05\x12\x13\n\x0fOT_BAYESIAN_OPT\x10\x06\x12\x1b\n\x17OT_SENSITIVITY_ANALYSIS\x10\x07\x12\x11\n\rOT_NEVER_GRAD\x10\x08\x12\r\n\tOT_SMC_PY\x10\t\x12\x19\n\x15OT_WORKLIST_SCHEDULER\x10\n\"U\n\x08\x44\x61taType\x12\r\n\tDT_UNKOWN\x10\x00\x12\x0c\n\x08\x44T_INT32\x10\x01\x12\x0c\n\x08\x44T_INT64\x10\x02\x12\x0e\n\nDT_FLOAT32\x10\x03\x12\x0e\n\nDT_FLOAT64\x10\x04\"A\n\rDecisionParam\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.sight.x.proto.Value\"\xa5\x01\n\rDecisionPoint\x12\x14\n\x0c\x63hoice_label\x18\x01 \x01(\t\x12\x15\n\rchosen_option\x18\x02 \x01(\t\x12\x33\n\rchoice_params\x18\x03 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x32\n\x0cstate_params\x18\x04 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\"\x80\x01\n\x0f\x44\x65\x63isionOutcome\x12\x15\n\routcome_label\x18\x01 \x01(\t\x12\x0e\n\x06reward\x18\x02 \x01(\x02\x12\x10\n\x08\x64iscount\x18\x03 \x01(\x02\x12\x34\n\x0eoutcome_params\x18\x04 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParamb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sight.proto.sight_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DECISIONCONFIGURATIONSTART_CHOICECONFIGENTRY._options = None
  _DECISIONCONFIGURATIONSTART_CHOICECONFIGENTRY._serialized_options = b'8\001'
  _DECISIONCONFIGURATIONSTART_STATEATTRSENTRY._options = None
  _DECISIONCONFIGURATIONSTART_STATEATTRSENTRY._serialized_options = b'8\001'
  _DECISIONCONFIGURATIONSTART_ACTIONATTRSENTRY._options = None
  _DECISIONCONFIGURATIONSTART_ACTIONATTRSENTRY._serialized_options = b'8\001'
  _DECISIONCONFIGURATIONSTART_OUTCOMEATTRSENTRY._options = None
  _DECISIONCONFIGURATIONSTART_OUTCOMEATTRSENTRY._serialized_options = b'8\001'
  _ATTRIBUTE._serialized_start=117
  _ATTRIBUTE._serialized_end=156
  _OBJECT._serialized_start=159
  _OBJECT._serialized_end=1744
  _OBJECT_METRICS._serialized_start=1264
  _OBJECT_METRICS._serialized_end=1352
  _OBJECT_ORDER._serialized_start=1354
  _OBJECT_ORDER._serialized_end=1383
  _OBJECT_SUBTYPE._serialized_start=1386
  _OBJECT_SUBTYPE._serialized_end=1724
  _PROPOSEACTION._serialized_start=1747
  _PROPOSEACTION._serialized_end=1883
  _CONFIGURATIONSTART._serialized_start=1886
  _CONFIGURATIONSTART._serialized_end=2122
  _CONFIGURATIONSTART_SUBTYPE._serialized_start=2046
  _CONFIGURATIONSTART_SUBTYPE._serialized_end=2102
  _EXCEPTION._serialized_start=2124
  _EXCEPTION._serialized_end=2183
  _TENSOR._serialized_start=2186
  _TENSOR._serialized_end=2913
  _TENSOR_STRINGVALUES._serialized_start=2652
  _TENSOR_STRINGVALUES._serialized_end=2681
  _TENSOR_BYTESVALUES._serialized_start=2683
  _TENSOR_BYTESVALUES._serialized_end=2711
  _TENSOR_INT64VALUES._serialized_start=2713
  _TENSOR_INT64VALUES._serialized_end=2741
  _TENSOR_DOUBLEVALUES._serialized_start=2743
  _TENSOR_DOUBLEVALUES._serialized_end=2772
  _TENSOR_BOOLVALUES._serialized_start=2774
  _TENSOR_BOOLVALUES._serialized_end=2801
  _TENSOR_SUBTYPE._serialized_start=2803
  _TENSOR_SUBTYPE._serialized_end=2899
  _LINK._serialized_start=2916
  _LINK._serialized_end=3072
  _LINK_LINKTYPE._serialized_start=2998
  _LINK_LINKTYPE._serialized_end=3072
  _TENSORFLOWEXAMPLE._serialized_start=3075
  _TENSORFLOWEXAMPLE._serialized_end=3345
  _LOG._serialized_start=3347
  _LOG._serialized_end=3388
  _TEXT._serialized_start=3390
  _TEXT._serialized_end=3510
  _TEXT_SUBTYPE._serialized_start=3459
  _TEXT_SUBTYPE._serialized_end=3510
  _VALUE._serialized_start=3513
  _VALUE._serialized_end=3831
  _VALUE_SUBTYPE._serialized_start=3708
  _VALUE_SUBTYPE._serialized_end=3817
  _BLOCKSTART._serialized_start=3834
  _BLOCKSTART._serialized_end=5154
  _BLOCKSTART_SUBTYPE._serialized_start=4672
  _BLOCKSTART_SUBTYPE._serialized_end=5134
  _BLOCKEND._serialized_start=5157
  _BLOCKEND._serialized_end=6217
  _BLOCKEND_METRICS._serialized_start=5720
  _BLOCKEND_METRICS._serialized_end=5754
  _BLOCKEND_SUBTYPE._serialized_start=5757
  _BLOCKEND_SUBTYPE._serialized_end=6197
  _LISTSTART._serialized_start=6220
  _LISTSTART._serialized_end=6395
  _LISTSTART_SUBTYPE._serialized_start=6285
  _LISTSTART_SUBTYPE._serialized_end=6395
  _TENSORFLOWMODELTRAININGEPOCHSTART._serialized_start=6397
  _TENSORFLOWMODELTRAININGEPOCHSTART._serialized_end=6471
  _ATTRIBUTESTART._serialized_start=6473
  _ATTRIBUTESTART._serialized_end=6534
  _ATTRIBUTEEND._serialized_start=6536
  _ATTRIBUTEEND._serialized_end=6563
  _PARAMS._serialized_start=6566
  _PARAMS._serialized_end=7000
  _SIMULATIONSTART._serialized_start=7002
  _SIMULATIONSTART._serialized_end=7019
  _SIMULATIONPARAMETERSSTART._serialized_start=7021
  _SIMULATIONPARAMETERSSTART._serialized_end=7048
  _SIMULATIONTIMESTEPSTART._serialized_start=7051
  _SIMULATIONTIMESTEPSTART._serialized_end=7363
  _SIMULATIONTIMESTEPSTART_TIMESTEPUNITS._serialized_start=7226
  _SIMULATIONTIMESTEPSTART_TIMESTEPUNITS._serialized_end=7363
  _CONTINUOUSPROBDIST._serialized_start=7366
  _CONTINUOUSPROBDIST._serialized_end=7606
  _CONTINUOUSPROBDIST_GAUSSIAN._serialized_start=7514
  _CONTINUOUSPROBDIST_GAUSSIAN._serialized_end=7553
  _CONTINUOUSPROBDIST_UNIFORM._serialized_start=7555
  _CONTINUOUSPROBDIST_UNIFORM._serialized_end=7598
  _DISCRETEPROBDIST._serialized_start=7609
  _DISCRETEPROBDIST._serialized_end=7740
  _DISCRETEPROBDIST_UNIFORM._serialized_start=7689
  _DISCRETEPROBDIST_UNIFORM._serialized_end=7732
  _DECISIONCONFIGURATIONSTART._serialized_start=7743
  _DECISIONCONFIGURATIONSTART._serialized_end=11365
  _DECISIONCONFIGURATIONSTART_VIZIERCONFIG._serialized_start=8204
  _DECISIONCONFIGURATIONSTART_VIZIERCONFIG._serialized_end=8218
  _DECISIONCONFIGURATIONSTART_ACMECONFIG._serialized_start=8221
  _DECISIONCONFIGURATIONSTART_ACMECONFIG._serialized_end=8462
  _DECISIONCONFIGURATIONSTART_ACMECONFIG_ACMEAGENT._serialized_start=8320
  _DECISIONCONFIGURATIONSTART_ACMECONFIG_ACMEAGENT._serialized_end=8462
  _DECISIONCONFIGURATIONSTART_GENETICALGORITHMCONFIG._serialized_start=8464
  _DECISIONCONFIGURATIONSTART_GENETICALGORITHMCONFIG._serialized_end=8517
  _DECISIONCONFIGURATIONSTART_EXHAUSTIVESEARCHCONFIG._serialized_start=8519
  _DECISIONCONFIGURATIONSTART_EXHAUSTIVESEARCHCONFIG._serialized_end=8543
  _DECISIONCONFIGURATIONSTART_LLMCONFIG._serialized_start=8546
  _DECISIONCONFIGURATIONSTART_LLMCONFIG._serialized_end=8909
  _DECISIONCONFIGURATIONSTART_LLMCONFIG_LLMALGORITHM._serialized_start=8740
  _DECISIONCONFIGURATIONSTART_LLMCONFIG_LLMALGORITHM._serialized_end=8827
  _DECISIONCONFIGURATIONSTART_LLMCONFIG_LLMGOAL._serialized_start=8829
  _DECISIONCONFIGURATIONSTART_LLMCONFIG_LLMGOAL._serialized_end=8909
  _DECISIONCONFIGURATIONSTART_BAYESIANOPTCONFIG._serialized_start=8911
  _DECISIONCONFIGURATIONSTART_BAYESIANOPTCONFIG._serialized_end=8930
  _DECISIONCONFIGURATIONSTART_SENSITIVITYANALYSISCONFIG._serialized_start=8932
  _DECISIONCONFIGURATIONSTART_SENSITIVITYANALYSISCONFIG._serialized_end=8959
  _DECISIONCONFIGURATIONSTART_NEVERGRADCONFIG._serialized_start=8962
  _DECISIONCONFIGURATIONSTART_NEVERGRADCONFIG._serialized_end=9360
  _DECISIONCONFIGURATIONSTART_NEVERGRADCONFIG_NEVERGRADALGORITHM._serialized_start=9079
  _DECISIONCONFIGURATIONSTART_NEVERGRADCONFIG_NEVERGRADALGORITHM._serialized_end=9360
  _DECISIONCONFIGURATIONSTART_SMCPYCONFIG._serialized_start=9362
  _DECISIONCONFIGURATIONSTART_SMCPYCONFIG._serialized_end=9375
  _DECISIONCONFIGURATIONSTART_WORKLISTSCHEDULERCONFIG._serialized_start=9377
  _DECISIONCONFIGURATIONSTART_WORKLISTSCHEDULERCONFIG._serialized_end=9402
  _DECISIONCONFIGURATIONSTART_CHOICECONFIG._serialized_start=9405
  _DECISIONCONFIGURATIONSTART_CHOICECONFIG._serialized_end=10345
  _DECISIONCONFIGURATIONSTART_CHOICECONFIGENTRY._serialized_start=10347
  _DECISIONCONFIGURATIONSTART_CHOICECONFIGENTRY._serialized_end=10454
  _DECISIONCONFIGURATIONSTART_ATTRPROPS._serialized_start=10457
  _DECISIONCONFIGURATIONSTART_ATTRPROPS._serialized_end=10726
  _DECISIONCONFIGURATIONSTART_STATEATTRSENTRY._serialized_start=10728
  _DECISIONCONFIGURATIONSTART_STATEATTRSENTRY._serialized_end=10830
  _DECISIONCONFIGURATIONSTART_ACTIONATTRSENTRY._serialized_start=10832
  _DECISIONCONFIGURATIONSTART_ACTIONATTRSENTRY._serialized_end=10935
  _DECISIONCONFIGURATIONSTART_OUTCOMEATTRSENTRY._serialized_start=10937
  _DECISIONCONFIGURATIONSTART_OUTCOMEATTRSENTRY._serialized_end=11041
  _DECISIONCONFIGURATIONSTART_OPTIMIZERTYPE._serialized_start=11044
  _DECISIONCONFIGURATIONSTART_OPTIMIZERTYPE._serialized_end=11278
  _DECISIONCONFIGURATIONSTART_DATATYPE._serialized_start=11280
  _DECISIONCONFIGURATIONSTART_DATATYPE._serialized_end=11365
  _DECISIONPARAM._serialized_start=11367
  _DECISIONPARAM._serialized_end=11432
  _DECISIONPOINT._serialized_start=11435
  _DECISIONPOINT._serialized_end=11600
  _DECISIONOUTCOME._serialized_start=11603
  _DECISIONOUTCOME._serialized_end=11731
# @@protoc_insertion_point(module_scope)
