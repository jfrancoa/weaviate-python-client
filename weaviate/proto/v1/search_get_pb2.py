# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/search_get.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from weaviate.proto.v1 import base_pb2 as v1_dot_base__pb2
from weaviate.proto.v1 import properties_pb2 as v1_dot_properties__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13v1/search_get.proto\x12\x0bweaviate.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\rv1/base.proto\x1a\x13v1/properties.proto"\x9a\t\n\rSearchRequest\x12\x12\n\ncollection\x18\x01 \x01(\t\x12\x0e\n\x06tenant\x18\n \x01(\t\x12=\n\x11\x63onsistency_level\x18\x0b \x01(\x0e\x32\x1d.weaviate.v1.ConsistencyLevelH\x00\x88\x01\x01\x12\x37\n\nproperties\x18\x14 \x01(\x0b\x32\x1e.weaviate.v1.PropertiesRequestH\x01\x88\x01\x01\x12\x33\n\x08metadata\x18\x15 \x01(\x0b\x32\x1c.weaviate.v1.MetadataRequestH\x02\x88\x01\x01\x12+\n\x08group_by\x18\x16 \x01(\x0b\x32\x14.weaviate.v1.GroupByH\x03\x88\x01\x01\x12\r\n\x05limit\x18\x1e \x01(\r\x12\x0e\n\x06offset\x18\x1f \x01(\r\x12\x0f\n\x07\x61utocut\x18  \x01(\r\x12\r\n\x05\x61\x66ter\x18! \x01(\t\x12$\n\x07sort_by\x18" \x03(\x0b\x32\x13.weaviate.v1.SortBy\x12*\n\x07\x66ilters\x18( \x01(\x0b\x32\x14.weaviate.v1.FiltersH\x04\x88\x01\x01\x12/\n\rhybrid_search\x18) \x01(\x0b\x32\x13.weaviate.v1.HybridH\x05\x88\x01\x01\x12+\n\x0b\x62m25_search\x18* \x01(\x0b\x32\x11.weaviate.v1.BM25H\x06\x88\x01\x01\x12\x31\n\x0bnear_vector\x18+ \x01(\x0b\x32\x17.weaviate.v1.NearVectorH\x07\x88\x01\x01\x12\x31\n\x0bnear_object\x18, \x01(\x0b\x32\x17.weaviate.v1.NearObjectH\x08\x88\x01\x01\x12\x33\n\tnear_text\x18- \x01(\x0b\x32\x1b.weaviate.v1.NearTextSearchH\t\x88\x01\x01\x12\x35\n\nnear_image\x18. \x01(\x0b\x32\x1c.weaviate.v1.NearImageSearchH\n\x88\x01\x01\x12\x35\n\nnear_audio\x18/ \x01(\x0b\x32\x1c.weaviate.v1.NearAudioSearchH\x0b\x88\x01\x01\x12\x35\n\nnear_video\x18\x30 \x01(\x0b\x32\x1c.weaviate.v1.NearVideoSearchH\x0c\x88\x01\x01\x12\x36\n\ngenerative\x18< \x01(\x0b\x32\x1d.weaviate.v1.GenerativeSearchH\r\x88\x01\x01\x12(\n\x06rerank\x18= \x01(\x0b\x32\x13.weaviate.v1.RerankH\x0e\x88\x01\x01\x12\x18\n\x0cuses_123_api\x18\x64 \x01(\x08\x42\x02\x18\x01\x42\x14\n\x12_consistency_levelB\r\n\x0b_propertiesB\x0b\n\t_metadataB\x0b\n\t_group_byB\n\n\x08_filtersB\x10\n\x0e_hybrid_searchB\x0e\n\x0c_bm25_searchB\x0e\n\x0c_near_vectorB\x0e\n\x0c_near_objectB\x0c\n\n_near_textB\r\n\x0b_near_imageB\r\n\x0b_near_audioB\r\n\x0b_near_videoB\r\n\x0b_generativeB\t\n\x07_rerank"L\n\x07GroupBy\x12\x0c\n\x04path\x18\x01 \x03(\t\x12\x18\n\x10number_of_groups\x18\x02 \x01(\x05\x12\x19\n\x11objects_per_group\x18\x03 \x01(\x05")\n\x06SortBy\x12\x11\n\tascending\x18\x01 \x01(\x08\x12\x0c\n\x04path\x18\x02 \x03(\t"m\n\x10GenerativeSearch\x12\x1e\n\x16single_response_prompt\x18\x01 \x01(\t\x12\x1d\n\x15grouped_response_task\x18\x02 \x01(\t\x12\x1a\n\x12grouped_properties\x18\x03 \x03(\t"\xcc\x01\n\x0fMetadataRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\x08\x12\x0e\n\x06vector\x18\x02 \x01(\x08\x12\x1a\n\x12\x63reation_time_unix\x18\x03 \x01(\x08\x12\x1d\n\x15last_update_time_unix\x18\x04 \x01(\x08\x12\x10\n\x08\x64istance\x18\x05 \x01(\x08\x12\x11\n\tcertainty\x18\x06 \x01(\x08\x12\r\n\x05score\x18\x07 \x01(\x08\x12\x15\n\rexplain_score\x18\x08 \x01(\x08\x12\x15\n\ris_consistent\x18\t \x01(\x08"\xd1\x01\n\x11PropertiesRequest\x12\x1a\n\x12non_ref_properties\x18\x01 \x03(\t\x12\x39\n\x0eref_properties\x18\x02 \x03(\x0b\x32!.weaviate.v1.RefPropertiesRequest\x12?\n\x11object_properties\x18\x03 \x03(\x0b\x32$.weaviate.v1.ObjectPropertiesRequest\x12$\n\x1creturn_all_nonref_properties\x18\x0b \x01(\x08"\x8b\x01\n\x17ObjectPropertiesRequest\x12\x11\n\tprop_name\x18\x01 \x01(\t\x12\x1c\n\x14primitive_properties\x18\x02 \x03(\t\x12?\n\x11object_properties\x18\x03 \x03(\x0b\x32$.weaviate.v1.ObjectPropertiesRequest"\xfc\x01\n\x06Hybrid\x12\r\n\x05query\x18\x01 \x01(\t\x12\x12\n\nproperties\x18\x02 \x03(\t\x12\x12\n\x06vector\x18\x03 \x03(\x02\x42\x02\x18\x01\x12\r\n\x05\x61lpha\x18\x04 \x01(\x02\x12\x33\n\x0b\x66usion_type\x18\x05 \x01(\x0e\x32\x1e.weaviate.v1.Hybrid.FusionType\x12\x14\n\x0cvector_bytes\x18\x06 \x01(\x0c"a\n\nFusionType\x12\x1b\n\x17\x46USION_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x46USION_TYPE_RANKED\x10\x01\x12\x1e\n\x1a\x46USION_TYPE_RELATIVE_SCORE\x10\x02"\xad\x02\n\x0eNearTextSearch\x12\r\n\x05query\x18\x01 \x03(\t\x12\x16\n\tcertainty\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x15\n\x08\x64istance\x18\x03 \x01(\x01H\x01\x88\x01\x01\x12\x36\n\x07move_to\x18\x04 \x01(\x0b\x32 .weaviate.v1.NearTextSearch.MoveH\x02\x88\x01\x01\x12\x38\n\tmove_away\x18\x05 \x01(\x0b\x32 .weaviate.v1.NearTextSearch.MoveH\x03\x88\x01\x01\x1a\x36\n\x04Move\x12\r\n\x05\x66orce\x18\x01 \x01(\x02\x12\x10\n\x08\x63oncepts\x18\x02 \x03(\t\x12\r\n\x05uuids\x18\x03 \x03(\tB\x0c\n\n_certaintyB\x0b\n\t_distanceB\n\n\x08_move_toB\x0c\n\n_move_away"j\n\x0fNearImageSearch\x12\r\n\x05image\x18\x01 \x01(\t\x12\x16\n\tcertainty\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x15\n\x08\x64istance\x18\x03 \x01(\x01H\x01\x88\x01\x01\x42\x0c\n\n_certaintyB\x0b\n\t_distance"j\n\x0fNearAudioSearch\x12\r\n\x05\x61udio\x18\x01 \x01(\t\x12\x16\n\tcertainty\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x15\n\x08\x64istance\x18\x03 \x01(\x01H\x01\x88\x01\x01\x42\x0c\n\n_certaintyB\x0b\n\t_distance"j\n\x0fNearVideoSearch\x12\r\n\x05video\x18\x01 \x01(\t\x12\x16\n\tcertainty\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x15\n\x08\x64istance\x18\x03 \x01(\x01H\x01\x88\x01\x01\x42\x0c\n\n_certaintyB\x0b\n\t_distance")\n\x04\x42M25\x12\r\n\x05query\x18\x01 \x01(\t\x12\x12\n\nproperties\x18\x02 \x03(\t"\xb1\x01\n\x14RefPropertiesRequest\x12\x1a\n\x12reference_property\x18\x01 \x01(\t\x12\x32\n\nproperties\x18\x02 \x01(\x0b\x32\x1e.weaviate.v1.PropertiesRequest\x12.\n\x08metadata\x18\x03 \x01(\x0b\x32\x1c.weaviate.v1.MetadataRequest\x12\x19\n\x11target_collection\x18\x04 \x01(\t"\x80\x01\n\nNearVector\x12\x12\n\x06vector\x18\x01 \x03(\x02\x42\x02\x18\x01\x12\x16\n\tcertainty\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x15\n\x08\x64istance\x18\x03 \x01(\x01H\x01\x88\x01\x01\x12\x14\n\x0cvector_bytes\x18\x04 \x01(\x0c\x42\x0c\n\n_certaintyB\x0b\n\t_distance"b\n\nNearObject\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\tcertainty\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x15\n\x08\x64istance\x18\x03 \x01(\x01H\x01\x88\x01\x01\x42\x0c\n\n_certaintyB\x0b\n\t_distance"8\n\x06Rerank\x12\x10\n\x08property\x18\x01 \x01(\t\x12\x12\n\x05query\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_query"\xc3\x01\n\x0bSearchReply\x12\x0c\n\x04took\x18\x01 \x01(\x02\x12*\n\x07results\x18\x02 \x03(\x0b\x32\x19.weaviate.v1.SearchResult\x12&\n\x19generative_grouped_result\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x34\n\x10group_by_results\x18\x04 \x03(\x0b\x32\x1a.weaviate.v1.GroupByResultB\x1c\n\x1a_generative_grouped_result"\x1c\n\x0bRerankReply\x12\r\n\x05score\x18\x01 \x01(\x01"!\n\x0fGenerativeReply\x12\x0e\n\x06result\x18\x01 \x01(\t"\x90\x02\n\rGroupByResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cmin_distance\x18\x02 \x01(\x02\x12\x14\n\x0cmax_distance\x18\x03 \x01(\x02\x12\x19\n\x11number_of_objects\x18\x04 \x01(\x03\x12*\n\x07objects\x18\x05 \x03(\x0b\x32\x19.weaviate.v1.SearchResult\x12-\n\x06rerank\x18\x06 \x01(\x0b\x32\x18.weaviate.v1.RerankReplyH\x00\x88\x01\x01\x12\x35\n\ngenerative\x18\x07 \x01(\x0b\x32\x1c.weaviate.v1.GenerativeReplyH\x01\x88\x01\x01\x42\t\n\x07_rerankB\r\n\x0b_generative"p\n\x0cSearchResult\x12\x31\n\nproperties\x18\x01 \x01(\x0b\x32\x1d.weaviate.v1.PropertiesResult\x12-\n\x08metadata\x18\x02 \x01(\x0b\x32\x1b.weaviate.v1.MetadataResult"\xc8\x04\n\x0eMetadataResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\x06vector\x18\x02 \x03(\x02\x42\x02\x18\x01\x12\x1a\n\x12\x63reation_time_unix\x18\x03 \x01(\x03\x12"\n\x1a\x63reation_time_unix_present\x18\x04 \x01(\x08\x12\x1d\n\x15last_update_time_unix\x18\x05 \x01(\x03\x12%\n\x1dlast_update_time_unix_present\x18\x06 \x01(\x08\x12\x10\n\x08\x64istance\x18\x07 \x01(\x02\x12\x18\n\x10\x64istance_present\x18\x08 \x01(\x08\x12\x11\n\tcertainty\x18\t \x01(\x02\x12\x19\n\x11\x63\x65rtainty_present\x18\n \x01(\x08\x12\r\n\x05score\x18\x0b \x01(\x02\x12\x15\n\rscore_present\x18\x0c \x01(\x08\x12\x15\n\rexplain_score\x18\r \x01(\t\x12\x1d\n\x15\x65xplain_score_present\x18\x0e \x01(\x08\x12\x1a\n\ris_consistent\x18\x0f \x01(\x08H\x00\x88\x01\x01\x12\x12\n\ngenerative\x18\x10 \x01(\t\x12\x1a\n\x12generative_present\x18\x11 \x01(\x08\x12\x1d\n\x15is_consistent_present\x18\x12 \x01(\x08\x12\x14\n\x0cvector_bytes\x18\x13 \x01(\x0c\x12\x13\n\x0bid_as_bytes\x18\x14 \x01(\x0c\x12\x14\n\x0crerank_score\x18\x15 \x01(\x01\x12\x1c\n\x14rerank_score_present\x18\x16 \x01(\x08\x42\x10\n\x0e_is_consistent"\x9d\x05\n\x10PropertiesResult\x12\x37\n\x12non_ref_properties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.StructB\x02\x18\x01\x12\x33\n\tref_props\x18\x02 \x03(\x0b\x32 .weaviate.v1.RefPropertiesResult\x12\x19\n\x11target_collection\x18\x03 \x01(\t\x12-\n\x08metadata\x18\x04 \x01(\x0b\x32\x1b.weaviate.v1.MetadataResult\x12G\n\x17number_array_properties\x18\x05 \x03(\x0b\x32".weaviate.v1.NumberArrayPropertiesB\x02\x18\x01\x12\x41\n\x14int_array_properties\x18\x06 \x03(\x0b\x32\x1f.weaviate.v1.IntArrayPropertiesB\x02\x18\x01\x12\x43\n\x15text_array_properties\x18\x07 \x03(\x0b\x32 .weaviate.v1.TextArrayPropertiesB\x02\x18\x01\x12I\n\x18\x62oolean_array_properties\x18\x08 \x03(\x0b\x32#.weaviate.v1.BooleanArrayPropertiesB\x02\x18\x01\x12<\n\x11object_properties\x18\t \x03(\x0b\x32\x1d.weaviate.v1.ObjectPropertiesB\x02\x18\x01\x12G\n\x17object_array_properties\x18\n \x03(\x0b\x32".weaviate.v1.ObjectArrayPropertiesB\x02\x18\x01\x12.\n\rnon_ref_props\x18\x0b \x01(\x0b\x32\x17.weaviate.v1.Properties"[\n\x13RefPropertiesResult\x12\x31\n\nproperties\x18\x01 \x03(\x0b\x32\x1d.weaviate.v1.PropertiesResult\x12\x11\n\tprop_name\x18\x02 \x01(\tBs\n#io.weaviate.client.grpc.protocol.v1B\x16WeaviateProtoSearchGetZ4github.com/weaviate/weaviate/grpc/generated;protocolb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.search_get_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n#io.weaviate.client.grpc.protocol.v1B\026WeaviateProtoSearchGetZ4github.com/weaviate/weaviate/grpc/generated;protocol"
    _SEARCHREQUEST.fields_by_name["uses_123_api"]._options = None
    _SEARCHREQUEST.fields_by_name["uses_123_api"]._serialized_options = b"\030\001"
    _HYBRID.fields_by_name["vector"]._options = None
    _HYBRID.fields_by_name["vector"]._serialized_options = b"\030\001"
    _NEARVECTOR.fields_by_name["vector"]._options = None
    _NEARVECTOR.fields_by_name["vector"]._serialized_options = b"\030\001"
    _METADATARESULT.fields_by_name["vector"]._options = None
    _METADATARESULT.fields_by_name["vector"]._serialized_options = b"\030\001"
    _PROPERTIESRESULT.fields_by_name["non_ref_properties"]._options = None
    _PROPERTIESRESULT.fields_by_name["non_ref_properties"]._serialized_options = b"\030\001"
    _PROPERTIESRESULT.fields_by_name["number_array_properties"]._options = None
    _PROPERTIESRESULT.fields_by_name["number_array_properties"]._serialized_options = b"\030\001"
    _PROPERTIESRESULT.fields_by_name["int_array_properties"]._options = None
    _PROPERTIESRESULT.fields_by_name["int_array_properties"]._serialized_options = b"\030\001"
    _PROPERTIESRESULT.fields_by_name["text_array_properties"]._options = None
    _PROPERTIESRESULT.fields_by_name["text_array_properties"]._serialized_options = b"\030\001"
    _PROPERTIESRESULT.fields_by_name["boolean_array_properties"]._options = None
    _PROPERTIESRESULT.fields_by_name["boolean_array_properties"]._serialized_options = b"\030\001"
    _PROPERTIESRESULT.fields_by_name["object_properties"]._options = None
    _PROPERTIESRESULT.fields_by_name["object_properties"]._serialized_options = b"\030\001"
    _PROPERTIESRESULT.fields_by_name["object_array_properties"]._options = None
    _PROPERTIESRESULT.fields_by_name["object_array_properties"]._serialized_options = b"\030\001"
    _globals["_SEARCHREQUEST"]._serialized_start = 103
    _globals["_SEARCHREQUEST"]._serialized_end = 1281
    _globals["_GROUPBY"]._serialized_start = 1283
    _globals["_GROUPBY"]._serialized_end = 1359
    _globals["_SORTBY"]._serialized_start = 1361
    _globals["_SORTBY"]._serialized_end = 1402
    _globals["_GENERATIVESEARCH"]._serialized_start = 1404
    _globals["_GENERATIVESEARCH"]._serialized_end = 1513
    _globals["_METADATAREQUEST"]._serialized_start = 1516
    _globals["_METADATAREQUEST"]._serialized_end = 1720
    _globals["_PROPERTIESREQUEST"]._serialized_start = 1723
    _globals["_PROPERTIESREQUEST"]._serialized_end = 1932
    _globals["_OBJECTPROPERTIESREQUEST"]._serialized_start = 1935
    _globals["_OBJECTPROPERTIESREQUEST"]._serialized_end = 2074
    _globals["_HYBRID"]._serialized_start = 2077
    _globals["_HYBRID"]._serialized_end = 2329
    _globals["_HYBRID_FUSIONTYPE"]._serialized_start = 2232
    _globals["_HYBRID_FUSIONTYPE"]._serialized_end = 2329
    _globals["_NEARTEXTSEARCH"]._serialized_start = 2332
    _globals["_NEARTEXTSEARCH"]._serialized_end = 2633
    _globals["_NEARTEXTSEARCH_MOVE"]._serialized_start = 2526
    _globals["_NEARTEXTSEARCH_MOVE"]._serialized_end = 2580
    _globals["_NEARIMAGESEARCH"]._serialized_start = 2635
    _globals["_NEARIMAGESEARCH"]._serialized_end = 2741
    _globals["_NEARAUDIOSEARCH"]._serialized_start = 2743
    _globals["_NEARAUDIOSEARCH"]._serialized_end = 2849
    _globals["_NEARVIDEOSEARCH"]._serialized_start = 2851
    _globals["_NEARVIDEOSEARCH"]._serialized_end = 2957
    _globals["_BM25"]._serialized_start = 2959
    _globals["_BM25"]._serialized_end = 3000
    _globals["_REFPROPERTIESREQUEST"]._serialized_start = 3003
    _globals["_REFPROPERTIESREQUEST"]._serialized_end = 3180
    _globals["_NEARVECTOR"]._serialized_start = 3183
    _globals["_NEARVECTOR"]._serialized_end = 3311
    _globals["_NEAROBJECT"]._serialized_start = 3313
    _globals["_NEAROBJECT"]._serialized_end = 3411
    _globals["_RERANK"]._serialized_start = 3413
    _globals["_RERANK"]._serialized_end = 3469
    _globals["_SEARCHREPLY"]._serialized_start = 3472
    _globals["_SEARCHREPLY"]._serialized_end = 3667
    _globals["_RERANKREPLY"]._serialized_start = 3669
    _globals["_RERANKREPLY"]._serialized_end = 3697
    _globals["_GENERATIVEREPLY"]._serialized_start = 3699
    _globals["_GENERATIVEREPLY"]._serialized_end = 3732
    _globals["_GROUPBYRESULT"]._serialized_start = 3735
    _globals["_GROUPBYRESULT"]._serialized_end = 4007
    _globals["_SEARCHRESULT"]._serialized_start = 4009
    _globals["_SEARCHRESULT"]._serialized_end = 4121
    _globals["_METADATARESULT"]._serialized_start = 4124
    _globals["_METADATARESULT"]._serialized_end = 4708
    _globals["_PROPERTIESRESULT"]._serialized_start = 4711
    _globals["_PROPERTIESRESULT"]._serialized_end = 5380
    _globals["_REFPROPERTIESRESULT"]._serialized_start = 5382
    _globals["_REFPROPERTIESRESULT"]._serialized_end = 5473
# @@protoc_insertion_point(module_scope)
