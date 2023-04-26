from enum import Enum, IntEnum

MAX_COUNT_FOR_INITIAL_LOG = 10
DISCOVER_DEFAULT_FRESH_BRANCH_COUNT = 10

PICK_FIRST_ROOT: int = 0
PICK_LAST_ROOT: int = -1


class SyncToRemoteStatuses(IntEnum):
    NO_REMOTES = 0
    UNTRACKED = 1
    IN_SYNC_WITH_REMOTE = 2
    BEHIND_REMOTE = 3
    AHEAD_OF_REMOTE = 4
    DIVERGED_FROM_AND_OLDER_THAN_REMOTE = 5
    DIVERGED_FROM_AND_NEWER_THAN_REMOTE = 6


class GitFormatPatterns(Enum):
    AUTHOR_NAME = "%aN"
    AUTHOR_EMAIL = "%aE"
    AUTHOR_DATE = "%ai"
    RAW_BODY = "%B"
