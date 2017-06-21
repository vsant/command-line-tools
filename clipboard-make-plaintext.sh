#!/bin/bash

pbpaste | pbcopy

osascript <<-EOT
  tell application "System Events"
    keystroke "v" using {command down}
  end tell
EOT
