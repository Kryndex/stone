# Auto-generated by Babel (Do not modify)
from dropbox import arg_struct_parser as asp

# We use an identity function because we don't need to mutate the return value
# of the parser in any way.
def identity(x):
    return x

files_file_target_validator = asp.Record(
    # Path from root. Should be an empty string for root.

    ('path', asp.StringB()),
    # Revision of target file.

    ('rev', asp.StringB()),
)

files_file_info_validator = asp.Record(
    # Name of file.

    ('name', asp.StringB()),
)

files_sub_error_validator = asp.Record(
    # A code indicating the type of error.

    ('reason', asp.StringB()),
)

files_download_error_validator = asp.Variant(
    ('disallowed', identity, files_sub_error_validator),
    ('no_file', identity, files_sub_error_validator),
)

files_upload_session_start_validator = asp.Record(
    # A unique identifier for the upload session.

    ('upload_id', asp.StringB()),
)

files_upload_append_validator = asp.Record(
    # Identifies the upload session to append data to.

    ('upload_id', asp.StringB()),
    # The offset into the file of the current chunk of data being uploaded. It
    # can also be thought of as the amount of data that has been uploaded so
    # far. We use the offset as a sanity check.

    ('offset', asp.Nat()),
)

files_incorrect_offset_error_validator = asp.Record(
    ('correct_offset', asp.Nat()),
)

files_upload_append_error_validator = asp.Variant(
    # :field:`upload_id` was not found.

    ('not_found', identity, object()),
    # Upload session was closed.

    ('closed', identity, object()),
    ('incorrect_offset', identity, files_incorrect_offset_error_validator),
)

files_update_parent_rev_validator = asp.Record(
    ('parent_rev', asp.StringB()),
)

files_conflict_policy_validator = asp.Variant(
    # On a conflict, the target is overridden.

    ('overwrite', identity, object()),
    # On a conflict, the upload is rejected. You can call the :route:`Upload`
    # endpoint again and attempt a different path.

    ('add', identity, object()),
    # On a conflict, only overwrite the target if the parent_rev matches.

    ('update', identity, files_update_parent_rev_validator),
)

files_upload_commit_validator = asp.Record(
    # Path in the user's Dropbox to save the file.

    ('path', asp.StringB()),
    # The course of action to take if a file already exists at :field:`path`.

    ('mode', files_conflict_policy_validator),
    # If specified, the current chunk of data should be appended to an existing
    # upload session.

    ('append_to', files_upload_append_validator),
    # Whether the file should be autorenamed in the event of a conflict.

    ('autorename', asp.Boolean(), False),
    # Self reported time of when this file was created or modified.

    ('client_modified_utc', asp.Nullable(asp.Nat()), None),
    # Whether the devices that the user has linked should notify them of the new
    # or updated file.

    ('mute', asp.Boolean(), False),
)

files_conflict_reason_validator = asp.Variant(
    # Conflict with a folder.

    ('folder', identity, object()),
    # Conflict with a file.

    ('file', identity, object()),
    # Could not autorename.

    ('autorename_failed', identity, object()),
)

files_conflict_error_validator = asp.Record(
    ('reason', files_conflict_reason_validator),
)

files_upload_commit_error_validator = asp.Variant(
    ('conflict', identity, files_conflict_error_validator),
    # User does not have permission to write in the folder. An example of this
    # is if the folder is a read-only shared folder.

    ('no_write_permission', identity, object()),
    # User does not have sufficient space quota to save the file.

    ('insufficient_quota', identity, object()),
)
