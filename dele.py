to_replace = ["[", "]", '"', ",", "|", "^", "0.0.0.0 ", "%20", r"%20%25**)(**@", "scammer-01=https://", "127.0.0.1 ", "localhost", "*.", "^$ctag=user_child", "( \ . | ^ )", "http://", "https://", ".", "HOST-KEYWORD, ", ", reject", "DOMAIN, "]

not_start_with = ["-", "."]

hosts = """
127.0.0.1 localhost
127.0.0.1 localhost.localdomain
127.0.0.1 local
255.255.255.255 broadcasthost
::1 localhost
::1 ip6-localhost
::1 ip6-loopback
fe80::1%lo0 localhost
ff00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
127.0.0.1 android
127.0.0.1 local
127.0.0.1 localhost
255.255.255.255 broadcasthost
:1 android
:1 local
:1 localhost
:1 localhost-ipv6
"""