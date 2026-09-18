#!/bin/bash
# Git credential helper that pulls the token live from glab's own config
# instead of storing it in any repo's .git/config.
if [ "$1" = "get" ]; then
  TOKEN=$(glab config get token --host git.avada.net 2>/dev/null)
  echo "username=oauth2"
  echo "password=${TOKEN}"
fi
