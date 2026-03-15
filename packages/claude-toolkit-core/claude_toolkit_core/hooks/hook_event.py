from enum import Enum


class HookEvent(str, Enum):
    CONFIG_CHANGE = "ConfigChange"
    NOTIFICATION = "Notification"
    PERMISSION_REQUEST = "PermissionRequest"
    POST_COMPACT = "PostCompact"
    POST_TOOL_USE = "PostToolUse"
    POST_TOOL_USE_FAILURE = "PostToolUseFailure"
    PRE_COMPACT = "PreCompact"
    PRE_TOOL_USE = "PreToolUse"
    SESSION_END = "SessionEnd"
    SESSION_START = "SessionStart"
    STOP = "Stop"
    SUBAGENT_START = "SubagentStart"
    SUBAGENT_STOP = "SubagentStop"
    TASK_COMPLETED = "TaskCompleted"
    USER_PROMPT_SUBMIT = "UserPromptSubmit"
    WORKTREE_CREATE = "WorktreeCreate"
    WORKTREE_REMOVE = "WorktreeRemove"
