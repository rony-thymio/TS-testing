---
title: Leader and followers
level: 3
age: 14+
needs: 2 or more wireless robots paired to the same dongle (see "Pair wireless robots")
robots: 2 or more on the same dongle
author: Thymio Suite activities
---
## The story
A team of robots works together: the leader decides, the followers obey. In Aseba, robots on the same dongle can send **events** to each other.

## Your goal
When you press a button on the leader robot, all the robots of the group show the same colour and drive the same way.

## Step by step
1. In the **Events** panel of the Aseba editor, create a global event `order` with 1 value.
2. Leader: in each button event, `emit order [n]` with a number for the order (1 forward, 2 left, 3 right, 0 stop) and obey it yourself.
3. Followers: `onevent order` reads the number in `event.args[0]` and applies it.
4. Open the Aseba editor with all the robots: each robot has its own tab. Write the leader program in the first tab and the follower program in the others, then click "Run all".

## Hints
1. All robots on the same dongle form a group and share the global events.
2. A subroutine avoids writing the same code twice: `sub apply` … then `callsub apply`.
3. `emit` sends the event to the other robots, not to the sender: the leader must also obey its own order.

## To go further
Make the followers answer: each one emits `ready` when it has obeyed, and the leader counts the answers.
