# Learning Ansible Variables: My Lab Notes

This document contains my notes and findings from setting up a local Ansible playground to understand how variables, directory structures, and scopes work.

---

## 🏗️ What I Was Trying to Build

I wanted to set up a playbook that prints a custom greeting message to two different test servers: an Ubuntu server and a Rocky Linux server.

The goal was to move from a messy "everything-in-one-file" setup to a clean, production-grade structure using **Global (Playbook-scoped)** and **Local (Host-scoped)** variables.

---

## 📁 The Final Directory Structure

After refactoring everything, this is what my working project directory looks like:

```text
variables/
├── ansible.cfg          # Disables host key checking and sets default inventory
├── docker-compose.yaml  # Spins up the local Ubuntu and Rocky containers
├── hosts                # Clean inventory file (only IPs and ports)
├── playbook.yaml        # Main playbook logic
├── group_vars/
│   └── targets.yaml     # Shared credentials for all machines in the [targets] group
└── host_vars/
    ├── ubuntu-server.yaml  # Specific local variable for Ubuntu
    └── rocky-server.yaml   # Specific local variable for Rocky
```

---

## 📝 Code Breakdown

### 1. The Inventory File (`hosts`)

I stripped this down so it only contains the infrastructure mapping. No variables or passwords are left cluttering this file.

```ini
[targets]
ubuntu-server ansible_host=127.0.0.1 ansible_port=2221
rocky-server  ansible_host=127.0.0.1 ansible_port=2222
```

### 2. The Playbook (`playbook.yaml`)

This contains a play-scoped (global) variable called `greetings` and prints the output using the `debug` module.

```yaml
- name: testing var in playbook.yaml
  hosts: targets
  gather_facts: false
  vars:
    greetings: hi-this-from-the-greetings-variables-inside-playbook.yaml
  tasks:
    - name: printing the varibale-content of greeting
      ansible.builtin.debug:
        msg: "{{ greetings }} and {{ greeting }}"
```

### 3. Group Variables (`group_vars/targets.yaml`)

Because both containers use the same username and password, I put them in a group folder. The filename `targets.yaml` matches the `[targets]` group header inside the `hosts` file.

```yaml
---
ansible_user: root
ansible_password: ansiblepassword
```

### 4. Host Variables (`host_vars/`)

To give each server a unique message, I used host variables. The filenames match the specific server names inside the inventory file.

* `host_vars/ubuntu-server.yaml`:

```yaml
---
greeting: "Hello-from-ubuntu-server!"
```

* `host_vars/rocky-server.yaml`:

```yaml
---
greeting: "Hello-from-rocky-server!"
```

---

## ❌ Pitfalls & Errors I Handled

### 1. The Strict `group_vars` Folder Name

I learned that you cannot name the `group_vars` folder whatever you want. It is a strict Ansible convention. If you name it something else, Ansible completely ignores it.

### 2. The YAML Syntax Mistake (`=` vs `:`)

When I first created my `group_vars/targets.yaml`, I accidentally wrote it like an INI file using equals signs:

```ini
# WRONG WAY (Threw a "failed to combine variables" error!)
ansible_user=root
```

**Fix:** Files inside `group_vars` and `host_vars` must use strict YAML syntax (`key: value` with a space).

```yaml
# CORRECT WAY
ansible_user: root
```

---

## 🧠 Core Concepts I Mastered

* **Global vs Local Variables:** Variables written inside the playbook apply to everyone (Global). Variables inside `host_vars` apply only to that specific machine (Local).
* **Variable Precedence:** If a variable inside a playbook and a variable inside `host_vars` have the same name, the Host variable (local) wins because it is more specific.
* **Offline Execution:** I ran the playbook while Docker was down, and it still went green! This is because `gather_facts: false` was set, and the `debug` module runs locally on my own machine. It didn't need a live SSH connection to evaluate string text.
