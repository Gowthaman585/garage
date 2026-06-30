# Ansible `gather_facts`: What's Inside and Why It's Useful 🔍🛠️

Today while playing around with Ansible variables, I learned about `gather_facts` — the thing that runs automatically at the start of every playbook (unless you turn it off). I always saw the `[Gathering Facts]` task fly by in the output and ignored it, but today I actually dumped all the facts and looked through them. Turns out it's a goldmine of system info you can use in your playbooks. Here's my breakdown. 📝

---

## What is `gather_facts`?

It's a built-in Ansible task that connects to the target host and collects detailed information about it — OS, hardware, network, storage, environment variables, basically everything about the machine. All of this gets stored in a variable called `ansible_facts`, which you can then use anywhere in your playbook (conditions, templates, debug messages, etc).

### My Setup

**`inventory`**
```ini
[local]
localhost ansible_connection=local
```

**`ansible.cfg`**
```ini
[defaults]
inventory = ./inventory
host_key_checking = false
```

**`variable.yaml`** (basic structure)
```yaml
---
- name: working with variables
  hosts: all
  tasks:
    - name: dumping all the details
      debug:
        var: ansible_facts
```

Ran it with:
```bash
ansible-playbook variable.yaml
```

And it printed a **huge** JSON dump of facts about my own laptop (since I'm running it against `localhost`). Here's what I found inside, grouped by category.

---

## 📂 Categories of Facts I Found

### 1. OS & Distro Info
- `distribution`, `distribution_version`, `distribution_major_version` — what OS/version you're on (mine showed `Archlinux`)
- `os_family` — broader OS family grouping
- `lsb` — distro details like codename and description
- `pkg_mgr` — which package manager is available (`pacman` for me)
- `kernel`, `kernel_version` — exact kernel build running

**Useful for:** writing playbooks that behave differently depending on OS (e.g. use `apt` on Debian vs `pacman` on Arch).

---

### 2. Hardware Info
- `architecture` — CPU architecture (`x86_64`)
- `processor`, `processor_cores`, `processor_count`, `processor_vcpus`, `processor_threads_per_core` — full CPU breakdown
- `memtotal_mb`, `memfree_mb`, `memory_mb` — RAM stats (total/used/free, even swap)
- `bios_date`, `bios_vendor`, `bios_version` — BIOS details
- `product_name`, `product_version`, `system_vendor` — device model info (showed my laptop model directly!)
- `form_factor` — whether it's a laptop, server, etc.

**Useful for:** capacity checks before deploying something heavy, or hardware-specific configuration.

---

### 3. Network Info
- `all_ipv4_addresses`, `all_ipv6_addresses` — every IP on the machine
- `default_ipv4`, `default_ipv6` — the main active network interface details (gateway, subnet, MAC address, etc.)
- `interfaces` — list of all network interfaces (`wlan0`, `lo`, `enp2s0` in my case)
- Per-interface details (like `wlan0` block) — MTU, driver module, speed, full feature flags
- `dns` — nameservers and resolver options
- `fqdn`, `hostname`, `domain` — naming info

**Useful for:** firewall rules, generating config files with the right IP, or registering hosts dynamically.

---

### 4. Storage Info
- `devices` — full breakdown of physical disks (model, size, partitions, sectors)
- `mounts` — every mounted filesystem with size, used/available space, filesystem type, and mount options
- `device_links` — UUIDs and labels for each partition

**Useful for:** checking free disk space before running a deployment, or validating that a required mount exists.

---

### 5. Date & Time
- `date_time` block — full breakdown: current date, time, timezone, epoch, ISO8601 format, weekday, week number

**Useful for:** timestamping logs, scheduling logic, or naming backup files dynamically.

---

### 6. User & Environment Info
- `user_id`, `user_dir`, `user_shell`, `user_gid`, `user_uid` — info about the user running the playbook
- `env` — a full dump of environment variables (`PATH`, `HOME`, `LANG`, `SHELL`, etc.)
- `effective_user_id`, `real_user_id` — useful for permission-related logic

**Useful for:** picking the correct home directory, or running shell-specific commands (`fish` vs `bash`).

---

### 7. Virtualization & Security
- `virtualization_type`, `virtualization_role` — whether the host is a VM, container, or physical host
- `virtualization_tech_host` — what hypervisors are available (`kvm`, `virtualbox` showed up for me)
- `selinux`, `apparmor` — security module status
- `fips` — whether FIPS mode is enabled

**Useful for:** skipping virtualization-specific tasks on bare metal, or checking security posture.

---

### 8. System Services
- `service_mgr` — init/service manager in use (`systemd` here)
- `systemd` — detailed build features of systemd itself
- `uptime_seconds` — how long the system has been running

**Useful for:** conditionally restarting services depending on the service manager available.

---

## How I'll Actually Use This

Instead of just dumping everything, the real value is referencing **specific facts** inside conditions or templates. For example:

```yaml
- name: Show only the OS family
  debug:
    msg: "This machine is running {{ ansible_facts['os_family'] }}"

- name: Only run this task on Arch-based systems
  package:
    name: htop
    state: present
  when: ansible_facts['os_family'] == "Archlinux"
```

That's the real power — facts let your playbook **adapt automatically** to whatever machine it's running on, instead of hardcoding assumptions.

---

## Quick Reference: Most Useful Facts

| Fact | What it gives you |
|---|---|
| `ansible_facts['os_family']` | OS family (Debian, RedHat, Archlinux, etc.) |
| `ansible_facts['distribution']` | Exact distro name |
| `ansible_facts['default_ipv4']['address']` | Main IP address |
| `ansible_facts['memtotal_mb']` | Total RAM |
| `ansible_facts['processor_vcpus']` | Number of CPU threads |
| `ansible_facts['mounts']` | Disk usage per mount point |
| `ansible_facts['date_time']['iso8601']` | Current timestamp |
| `ansible_facts['hostname']` | Hostname of the machine |
| `ansible_facts['pkg_mgr']` | Package manager available |

---

## Reflections 💭

Before today I thought `gather_facts` was just Ansible "checking in" on the host and slowing things down a bit. Now I get why it's there — it gives every playbook a complete picture of the machine it's running on, without me writing a single shell command to check OS, IP, disk space, or anything else manually.

Next time I write a playbook, I want to actually use `when:` conditions based on these facts instead of assuming every host looks the same.

---

*Part of my ongoing Ansible learning notes on CachyOS / Arch Linux.*
