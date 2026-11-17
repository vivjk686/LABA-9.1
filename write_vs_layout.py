# -*- coding: utf-8 -*-
import os
import json

base_dir = r"C:\Users\User\OneDrive\Документи\лаби\LABA-9.1"
vs_dirs = [
    os.path.join(base_dir, ".vs", "LABA-9.1", "v17"),
    os.path.join(base_dir, ".vs", "LABA-9.1", "v18"),
    os.path.join(base_dir, ".vs", "LABA-9.1.slnx", "v17"),
    os.path.join(base_dir, ".vs", "LABA-9.1.slnx", "v18")
]

# Construct exact Visual Studio DocumentLayout structure
doc_layout = {
    "Version": 1,
    "WorkspaceRootPath": base_dir.replace("/", "\\") + "\\",
    "Documents": [
        {
            "AbsoluteMoniker": f"D:0:0:{{A9100001-78B8-55BB-BD56-E786907859BF}}|LABA-9.1\\LABA-9.1.vcxproj|{base_dir}\\LABA-9.1\\LABA-9.1.cpp||{{D0E1A5C6-B359-4E41-9B60-3365922C2A22}}",
            "RelativeMoniker": "D:0:0:{A9100001-78B8-55BB-BD56-E786907859BF}|LABA-9.1\\LABA-9.1.vcxproj|solutionrelative:LABA-9.1\\LABA-9.1.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
        },
        {
            "AbsoluteMoniker": f"D:0:0:{{B9100002-C24F-5E88-83AD-EB350CB9AF59}}|UnitTest9.1\\UnitTest9.1.vcxproj|{base_dir}\\UnitTest9.1\\UnitTest9.1.cpp||{{D0E1A5C6-B359-4E41-9B60-3365922C2A22}}",
            "RelativeMoniker": "D:0:0:{B9100002-C24F-5E88-83AD-EB350CB9AF59}|UnitTest9.1\\UnitTest9.1.vcxproj|solutionrelative:UnitTest9.1\\UnitTest9.1.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
        },
        {
            "AbsoluteMoniker": f"D:0:0:{{A9100001-78B8-55BB-BD56-E786907859BF}}|LABA-9.1\\LABA-9.1.vcxproj|{base_dir}\\LABA-9.1\\sum.cpp||{{D0E1A5C6-B359-4E41-9B60-3365922C2A22}}",
            "RelativeMoniker": "D:0:0:{A9100001-78B8-55BB-BD56-E786907859BF}|LABA-9.1\\LABA-9.1.vcxproj|solutionrelative:LABA-9.1\\sum.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
        },
        {
            "AbsoluteMoniker": f"D:0:0:{{A9100001-78B8-55BB-BD56-E786907859BF}}|LABA-9.1\\LABA-9.1.vcxproj|{base_dir}\\LABA-9.1\\dod.cpp||{{D0E1A5C6-B359-4E41-9B60-3365922C2A22}}",
            "RelativeMoniker": "D:0:0:{A9100001-78B8-55BB-BD56-E786907859BF}|LABA-9.1\\LABA-9.1.vcxproj|solutionrelative:LABA-9.1\\dod.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
        },
        {
            "AbsoluteMoniker": f"D:0:0:{{A9100001-78B8-55BB-BD56-E786907859BF}}|LABA-9.1\\LABA-9.1.vcxproj|{base_dir}\\LABA-9.1\\var.cpp||{{D0E1A5C6-B359-4E41-9B60-3365922C2A22}}",
            "RelativeMoniker": "D:0:0:{A9100001-78B8-55BB-BD56-E786907859BF}|LABA-9.1\\LABA-9.1.vcxproj|solutionrelative:LABA-9.1\\var.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
        }
    ],
    "DocumentGroupContainers": [
        {
            "Orientation": 0,
            "VerticalTabListWidth": 256,
            "DocumentGroups": [
                {
                    "DockedWidth": 200,
                    "SelectedChildIndex": 0,
                    "Children": [
                        {
                            "$type": "Document",
                            "DocumentIndex": 0,
                            "Title": "LABA-9.1.cpp",
                            "DocumentMoniker": f"{base_dir}\\LABA-9.1\\LABA-9.1.cpp",
                            "RelativeDocumentMoniker": "LABA-9.1\\LABA-9.1.cpp",
                            "ToolTip": f"{base_dir}\\LABA-9.1\\LABA-9.1.cpp",
                            "RelativeToolTip": "LABA-9.1\\LABA-9.1.cpp",
                            "ViewState": "AgIAAAAAAAAAAAAAAAAAABgAAAAgAAAAAAAAAA==",
                            "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
                            "WhenOpened": "2026-11-17T11:00:00Z",
                            "IsPinned": True,
                            "EditorCaption": ""
                        },
                        {
                            "$type": "Document",
                            "DocumentIndex": 1,
                            "Title": "UnitTest9.1.cpp",
                            "DocumentMoniker": f"{base_dir}\\UnitTest9.1\\UnitTest9.1.cpp",
                            "RelativeDocumentMoniker": "UnitTest9.1\\UnitTest9.1.cpp",
                            "ToolTip": f"{base_dir}\\UnitTest9.1\\UnitTest9.1.cpp",
                            "RelativeToolTip": "UnitTest9.1\\UnitTest9.1.cpp",
                            "ViewState": "AgIAAAAAAAAAAAAAAAAAAAIAAAAjAAAAAAAAAA==",
                            "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
                            "WhenOpened": "2026-11-17T11:00:01Z",
                            "IsPinned": True,
                            "EditorCaption": ""
                        },
                        {
                            "$type": "Document",
                            "DocumentIndex": 2,
                            "Title": "sum.cpp",
                            "DocumentMoniker": f"{base_dir}\\LABA-9.1\\sum.cpp",
                            "RelativeDocumentMoniker": "LABA-9.1\\sum.cpp",
                            "ToolTip": f"{base_dir}\\LABA-9.1\\sum.cpp",
                            "RelativeToolTip": "LABA-9.1\\sum.cpp",
                            "ViewState": "AgIAAAAAAAAAAAAAAAAAAAIAAAAjAAAAAAAAAA==",
                            "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
                            "WhenOpened": "2026-11-17T11:00:02Z",
                            "IsPinned": False,
                            "EditorCaption": ""
                        },
                        {
                            "$type": "Document",
                            "DocumentIndex": 3,
                            "Title": "dod.cpp",
                            "DocumentMoniker": f"{base_dir}\\LABA-9.1\\dod.cpp",
                            "RelativeDocumentMoniker": "LABA-9.1\\dod.cpp",
                            "ToolTip": f"{base_dir}\\LABA-9.1\\dod.cpp",
                            "RelativeToolTip": "LABA-9.1\\dod.cpp",
                            "ViewState": "AgIAAAAAAAAAAAAAAAAAAAIAAAAjAAAAAAAAAA==",
                            "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
                            "WhenOpened": "2026-11-17T11:00:03Z",
                            "IsPinned": False,
                            "EditorCaption": ""
                        },
                        {
                            "$type": "Document",
                            "DocumentIndex": 4,
                            "Title": "var.cpp",
                            "DocumentMoniker": f"{base_dir}\\LABA-9.1\\var.cpp",
                            "RelativeDocumentMoniker": "LABA-9.1\\var.cpp",
                            "ToolTip": f"{base_dir}\\LABA-9.1\\var.cpp",
                            "RelativeToolTip": "LABA-9.1\\var.cpp",
                            "ViewState": "AgIAAAAAAAAAAAAAAAAAAAIAAAAjAAAAAAAAAA==",
                            "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
                            "WhenOpened": "2026-11-17T11:00:04Z",
                            "IsPinned": False,
                            "EditorCaption": ""
                        },
                        {
                            "$type": "Bookmark",
                            "Name": "ST:1:0:{d212f56b-c48a-434c-a121-1c5d80b59b9f}"
                        }
                    ]
                }
            ]
        }
    ]
}

content_ascii = json.dumps(doc_layout, indent=2, ensure_ascii=True)

for d in vs_dirs:
    os.makedirs(d, exist_ok=True)
    fpath = os.path.join(d, "DocumentLayout.json")
    with open(fpath, "w", encoding="ascii") as f:
        f.write(content_ascii)
    print("Wrote valid DocumentLayout.json to:", fpath)

# Also write to mirrors
for mirror_base in [r"D:\лаби\LABA-9.1", r"C:\Users\User\OneDrive\Desktop\лаби\LABA-9.1"]:
    for sub in ["LABA-9.1/v17", "LABA-9.1/v18", "LABA-9.1.slnx/v17", "LABA-9.1.slnx/v18"]:
        target_dir = os.path.join(mirror_base, ".vs", *sub.split("/"))
        os.makedirs(target_dir, exist_ok=True)
        # Adapt workspace root path and document monikers for mirror
        mirror_layout = json.loads(content_ascii)
        mirror_layout["WorkspaceRootPath"] = mirror_base.replace("/", "\\") + "\\"
        for doc in mirror_layout["Documents"]:
            doc["AbsoluteMoniker"] = doc["AbsoluteMoniker"].replace(base_dir, mirror_base)
        for child in mirror_layout["DocumentGroupContainers"][0]["DocumentGroups"][0]["Children"]:
            if child.get("$type") == "Document":
                child["DocumentMoniker"] = child["DocumentMoniker"].replace(base_dir, mirror_base)
                child["ToolTip"] = child["ToolTip"].replace(base_dir, mirror_base)
        m_path = os.path.join(target_dir, "DocumentLayout.json")
        with open(m_path, "w", encoding="ascii") as f:
            json.dump(mirror_layout, f, indent=2, ensure_ascii=True)
        print("Wrote mirror DocumentLayout.json to:", m_path)
