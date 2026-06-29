#!/bin/bash
grep -E "^[^:]+:[^:]+:[^:]+ [^ ]+ sshd\[[0-9]+\]: (Accepted|Failed)" auth.log
