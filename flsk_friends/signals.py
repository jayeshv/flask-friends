import blinker

signals = blinker.Namespace()

follower_added = signals.signal("follower-added")

request_received = signals.signal("request-received")

request_accepted = signals.signal("request-accepted")

request_rejected = signals.signal("request-rejected")

