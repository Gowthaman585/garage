# 🚀 My First Ansible Win: Fixing Typos & Local Ping Success!

Hey everyone! Today I finally got my hands dirty with Ansible on my laptop (running CachyOS). Honestly, it was a bit of a rollercoaster at first because I was completely new to this, but I figured it out! Here is how my first lab experience went. 💻✨

---

## 🛑 The Initial Struggle (What went wrong)

I tried to follow a text tutorial from GitHub, but when I ran my first command, Ansible completely ignored my files and gave me a bunch of scary warnings about missing inventories. 🤦‍♂️

After looking closely at my terminal, I realized I made two classic beginner mistakes:
1. **The Ultimate Typo:** I named my configuration file `anisble.cfg` instead of `ansible.cfg`. Spotting that spelling mistake took me a minute! 😅
2. **Mixing Things Up:** I accidentally put my configuration settings and my target server names into a big jumble instead of splitting them up properly. 

---

## 🛠️ How I Fixed It

Ansible is super strict about where things go. It needs two distinct files, so I separated their jobs completely:

* **`ansible.cfg`** ➡️ This is the "blueprint" file. It tells Ansible how to behave and exactly where to look for my server lists.
* **`inventory`** ➡️ This is the "infrastructure map." It lists the machines I want to control. Since I'm using my own laptop, I set it to `localhost` and used `ansible_connection=local` so it stays safely inside my machine without hitting the network. 🔒

---

## 🎉 The Sweet Victory!

Once I fixed the spelling and separated the files, I ran the magic command to ping my local group:

```bash
ansible local -m ping
```
![ping result](ping-pong/ping-pong.png)
