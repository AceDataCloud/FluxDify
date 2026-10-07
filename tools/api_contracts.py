"""Published API contracts; source revisions are recorded in tests/parity-audit.json."""

TASK_PATH = "/flux/tasks"

ENDPOINTS = {
    "flux_generate_image": {
        "method": "POST",
        "path": "/flux/images",
        "operation": "generate",
        "schema": {
            "type": "object",
            "required": ["action", "prompt", "size"],
            "properties": {
                "size": {"type": "string"},
                "count": {"type": "number"},
                "model": {
                    "enum": [
                        "flux-dev",
                        "flux-pro",
                        "flux-kontext-pro",
                        "flux-kontext-max",
                        "flux-2-flex",
                        "flux-2-pro",
                        "flux-2-max",
                        "flux-2-klein",
                    ],
                    "type": "string",
                },
                "action": {"enum": ["generate", "edit"], "type": "string"},
                "prompt": {"type": "string"},
                "image_url": {"type": "string"},
                "callback_url": {"type": "string"},
                "async": {"type": "boolean"},
            },
        },
        "properties": {
            "size": {"type": "string"},
            "count": {"type": "number"},
            "model": {
                "enum": [
                    "flux-dev",
                    "flux-pro",
                    "flux-kontext-pro",
                    "flux-kontext-max",
                    "flux-2-flex",
                    "flux-2-pro",
                    "flux-2-max",
                    "flux-2-klein",
                ],
                "type": "string",
            },
            "action": {"enum": ["generate", "edit"], "type": "string"},
            "prompt": {"type": "string"},
            "image_url": {"type": "string"},
            "callback_url": {"type": "string"},
            "async": {"type": "boolean"},
        },
        "parameters": [],
        "defaults": {"model": "flux-dev", "size": "1024x1024", "count": 1},
        "fixed": {"action": "generate"},
        "allow_empty": [],
        "query_actions": [],
        "media_response": True,
    },
    "flux_edit_image": {
        "method": "POST",
        "path": "/flux/images",
        "operation": "edit",
        "schema": {
            "type": "object",
            "required": ["action", "prompt", "size"],
            "properties": {
                "size": {"type": "string"},
                "count": {"type": "number"},
                "model": {
                    "enum": [
                        "flux-dev",
                        "flux-pro",
                        "flux-kontext-pro",
                        "flux-kontext-max",
                        "flux-2-flex",
                        "flux-2-pro",
                        "flux-2-max",
                        "flux-2-klein",
                    ],
                    "type": "string",
                },
                "action": {"enum": ["generate", "edit"], "type": "string"},
                "prompt": {"type": "string"},
                "image_url": {"type": "string"},
                "callback_url": {"type": "string"},
                "async": {"type": "boolean"},
            },
        },
        "properties": {
            "size": {"type": "string"},
            "count": {"type": "number"},
            "model": {
                "enum": [
                    "flux-dev",
                    "flux-pro",
                    "flux-kontext-pro",
                    "flux-kontext-max",
                    "flux-2-flex",
                    "flux-2-pro",
                    "flux-2-max",
                    "flux-2-klein",
                ],
                "type": "string",
            },
            "action": {"enum": ["generate", "edit"], "type": "string"},
            "prompt": {"type": "string"},
            "image_url": {"type": "string"},
            "callback_url": {"type": "string"},
            "async": {"type": "boolean"},
        },
        "parameters": [],
        "defaults": {"model": "flux-kontext-pro", "size": "1:1", "count": 1},
        "fixed": {"action": "edit"},
        "allow_empty": [],
        "query_actions": [],
        "media_response": True,
    },
    "flux_generate_video": {
        "method": "POST",
        "path": "/flux/videos",
        "operation": "video",
        "schema": {
            "oneOf": [
                {
                    "oneOf": [
                        {
                            "properties": {
                                "prompt": {"type": "string"},
                                "aspect_ratio": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "enum": [
                                                "21:9",
                                                "2:1",
                                                "16:9",
                                                "4:3",
                                                "1:1",
                                                "3:4",
                                                "9:16",
                                                "9:21",
                                            ],
                                        },
                                        {"type": "string", "const": "auto"},
                                    ]
                                },
                                "duration": {
                                    "anyOf": [
                                        {"type": "integer", "maximum": 20, "minimum": 5},
                                        {"type": "string", "const": "auto"},
                                    ]
                                },
                                "resolution": {
                                    "type": "string",
                                    "enum": ["hd", "fhd", "qhd", "uhd"],
                                },
                                "version": {"type": "string", "const": "latest"},
                                "generate_audio": {"type": "boolean"},
                                "safety_tolerance": {"type": "integer", "maximum": 4, "minimum": 0},
                                "draft": {"type": "boolean"},
                                "mode": {"type": "string", "const": "t2v"},
                                "async": {"type": "boolean"},
                                "callback_url": {"type": "string", "format": "uri"},
                                "model": {"type": "string", "enum": ["flux-3"]},
                                "action": {"type": "string", "enum": ["generate"]},
                            },
                            "additionalProperties": False,
                            "type": "object",
                            "required": ["prompt", "mode"],
                        },
                        {
                            "properties": {
                                "prompt": {"type": "string"},
                                "aspect_ratio": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "enum": [
                                                "21:9",
                                                "2:1",
                                                "16:9",
                                                "4:3",
                                                "1:1",
                                                "3:4",
                                                "9:16",
                                                "9:21",
                                            ],
                                        },
                                        {"type": "string", "const": "auto"},
                                    ]
                                },
                                "duration": {
                                    "anyOf": [
                                        {"type": "integer", "maximum": 20, "minimum": 5},
                                        {"type": "string", "const": "auto"},
                                    ]
                                },
                                "resolution": {
                                    "type": "string",
                                    "enum": ["hd", "fhd", "qhd", "uhd"],
                                },
                                "version": {"type": "string", "const": "latest"},
                                "generate_audio": {"type": "boolean"},
                                "safety_tolerance": {"type": "integer", "maximum": 4, "minimum": 0},
                                "draft": {"type": "boolean"},
                                "mode": {"type": "string", "const": "i2v"},
                                "keyframes": {
                                    "anyOf": [
                                        {"type": "string"},
                                        {
                                            "prefixItems": [{"type": "number"}, {"type": "string"}],
                                            "type": "array",
                                            "maxItems": 2,
                                            "minItems": 2,
                                            "items": {
                                                "anyOf": [{"type": "number"}, {"type": "string"}]
                                            },
                                        },
                                        {"items": {"type": "string"}, "type": "array"},
                                        {
                                            "items": {
                                                "prefixItems": [
                                                    {"type": "number"},
                                                    {"type": "string"},
                                                ],
                                                "type": "array",
                                                "maxItems": 2,
                                                "minItems": 2,
                                                "items": {
                                                    "anyOf": [
                                                        {"type": "number"},
                                                        {"type": "string"},
                                                    ]
                                                },
                                            },
                                            "type": "array",
                                        },
                                    ]
                                },
                                "async": {"type": "boolean"},
                                "callback_url": {"type": "string", "format": "uri"},
                                "model": {"type": "string", "enum": ["flux-3"]},
                                "action": {"type": "string", "enum": ["generate"]},
                            },
                            "additionalProperties": False,
                            "type": "object",
                            "required": ["prompt", "mode", "keyframes"],
                        },
                        {
                            "properties": {
                                "prompt": {"type": "string"},
                                "aspect_ratio": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "enum": [
                                                "21:9",
                                                "2:1",
                                                "16:9",
                                                "4:3",
                                                "1:1",
                                                "3:4",
                                                "9:16",
                                                "9:21",
                                            ],
                                        },
                                        {"type": "string", "const": "auto"},
                                    ]
                                },
                                "duration": {
                                    "anyOf": [
                                        {"type": "integer", "maximum": 15, "minimum": 5},
                                        {"type": "string", "const": "auto"},
                                    ]
                                },
                                "resolution": {
                                    "type": "string",
                                    "enum": ["hd", "fhd", "qhd", "uhd"],
                                },
                                "version": {"type": "string", "const": "latest"},
                                "generate_audio": {"type": "boolean"},
                                "safety_tolerance": {"type": "integer", "maximum": 4, "minimum": 0},
                                "draft": {"type": "boolean"},
                                "mode": {"type": "string", "const": "v2v"},
                                "start_video": {"type": "string"},
                                "async": {"type": "boolean"},
                                "callback_url": {"type": "string", "format": "uri"},
                                "model": {"type": "string", "enum": ["flux-3"]},
                                "action": {"type": "string", "enum": ["generate"]},
                            },
                            "additionalProperties": False,
                            "type": "object",
                            "required": ["prompt", "mode", "start_video"],
                        },
                        {
                            "properties": {
                                "mode": {"type": "string", "const": "draft_enhance"},
                                "resolution": {
                                    "type": "string",
                                    "enum": ["hd", "fhd", "qhd", "uhd"],
                                },
                                "safety_tolerance": {"type": "integer", "maximum": 4, "minimum": 0},
                                "draft_task_id": {"type": "string"},
                                "async": {"type": "boolean"},
                                "callback_url": {"type": "string", "format": "uri"},
                                "model": {"type": "string", "enum": ["flux-3"]},
                                "action": {"type": "string", "enum": ["generate"]},
                            },
                            "additionalProperties": False,
                            "type": "object",
                            "required": ["mode", "draft_task_id"],
                        },
                    ],
                    "discriminator": {
                        "propertyName": "mode",
                        "mapping": {
                            "draft_enhance": "#/components/schemas/Flux3VideoDraftEnhanceInputs",
                            "i2v": "#/components/schemas/Flux3VideoI2VInputs",
                            "t2v": "#/components/schemas/Flux3VideoT2VInputs",
                            "v2v": "#/components/schemas/Flux3VideoV2VInputs",
                        },
                    },
                }
            ],
            "properties": {"action": {"type": "string", "enum": ["generate"]}},
        },
        "properties": {
            "action": {"type": "string", "enum": ["generate"]},
            "prompt": {"type": "string"},
            "aspect_ratio": {
                "anyOf": [
                    {
                        "type": "string",
                        "enum": ["21:9", "2:1", "16:9", "4:3", "1:1", "3:4", "9:16", "9:21"],
                    },
                    {"type": "string", "const": "auto"},
                ]
            },
            "duration": {
                "anyOf": [
                    {"type": "integer", "maximum": 20, "minimum": 5},
                    {"type": "string", "const": "auto"},
                ]
            },
            "resolution": {"type": "string", "enum": ["hd", "fhd", "qhd", "uhd"]},
            "version": {"type": "string", "enum": ["latest"]},
            "generate_audio": {"type": "boolean"},
            "safety_tolerance": {"type": "integer", "maximum": 4, "minimum": 0},
            "draft": {"type": "boolean"},
            "mode": {"type": "string", "enum": ["t2v", "i2v", "v2v", "draft_enhance"]},
            "async": {"type": "boolean"},
            "callback_url": {"type": "string", "format": "uri"},
            "model": {"type": "string", "enum": ["flux-3"]},
            "keyframes": {
                "anyOf": [
                    {"type": "string"},
                    {
                        "prefixItems": [{"type": "number"}, {"type": "string"}],
                        "type": "array",
                        "maxItems": 2,
                        "minItems": 2,
                        "items": {"anyOf": [{"type": "number"}, {"type": "string"}]},
                    },
                    {"items": {"type": "string"}, "type": "array"},
                    {
                        "items": {
                            "prefixItems": [{"type": "number"}, {"type": "string"}],
                            "type": "array",
                            "maxItems": 2,
                            "minItems": 2,
                            "items": {"anyOf": [{"type": "number"}, {"type": "string"}]},
                        },
                        "type": "array",
                    },
                ]
            },
            "start_video": {"type": "string"},
            "draft_task_id": {"type": "string"},
        },
        "parameters": [],
        "defaults": {"model": "flux-3", "action": "generate", "mode": "t2v"},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "flux_task_retrieve": {
        "method": "POST",
        "path": "/flux/tasks",
        "operation": "task",
        "schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}},
                "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
            },
        },
        "properties": {
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}},
            "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
        },
        "parameters": [],
        "defaults": {"wait_seconds": 0},
        "fixed": {},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
    "flux_tasks_retrieve_batch": {
        "method": "POST",
        "path": "/flux/tasks",
        "operation": "batch",
        "schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
                "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
            },
            "required": ["action", "ids"],
        },
        "properties": {
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
            "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {"action": "retrieve_batch"},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
}
