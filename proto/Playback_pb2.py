# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playback.proto
"""Generated protocol buffer code."""
import ContextTrack_pb2 as context__track__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name="playback.proto",
    package="spotify.player.proto.transfer",
    syntax="proto2",
    serialized_options=b"\n\024com.spotify.transferH\002",
    create_key=_descriptor._internal_create_key,
    serialized_pb=
    b'\n\x0eplayback.proto\x12\x1dspotify.player.proto.transfer\x1a\x13\x63ontext_track.proto"\xa5\x01\n\x08Playback\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12 \n\x18position_as_of_timestamp\x18\x02 \x01(\x05\x12\x16\n\x0eplayback_speed\x18\x03 \x01(\x01\x12\x11\n\tis_paused\x18\x04 \x01(\x08\x12\x39\n\rcurrent_track\x18\x05 \x01(\x0b\x32".spotify.player.proto.ContextTrackB\x18\n\x14\x63om.spotify.transferH\x02',
    dependencies=[
        context__track__pb2.DESCRIPTOR,
    ],
)

_PLAYBACK = _descriptor.Descriptor(
    name="Playback",
    full_name="spotify.player.proto.transfer.Playback",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="timestamp",
            full_name="spotify.player.proto.transfer.Playback.timestamp",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="position_as_of_timestamp",
            full_name=
            "spotify.player.proto.transfer.Playback.position_as_of_timestamp",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="playback_speed",
            full_name="spotify.player.proto.transfer.Playback.playback_speed",
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="is_paused",
            full_name="spotify.player.proto.transfer.Playback.is_paused",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="current_track",
            full_name="spotify.player.proto.transfer.Playback.current_track",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=71,
    serialized_end=236,
)

_PLAYBACK.fields_by_name[
    "current_track"].message_type = context__track__pb2._CONTEXTTRACK
DESCRIPTOR.message_types_by_name["Playback"] = _PLAYBACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Playback = _reflection.GeneratedProtocolMessageType(
    "Playback",
    (_message.Message, ),
    {
        "DESCRIPTOR": _PLAYBACK,
        "__module__": "playback_pb2"
        # @@protoc_insertion_point(class_scope:spotify.player.proto.transfer.Playback)
    },
)
_sym_db.RegisterMessage(Playback)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
