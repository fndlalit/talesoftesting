---
title: "Session Based Programming 1.0"
date: 2016-12-12 18:14:30 +0530
categories: [Uncategorized]
---

With my experience as an Agile tester so far, one thing I see organisations still struggling with or trying to get better at are the **estimations**.While thinking deeply about what makes our estimations go wrong I realised that there is still a lot we do in projects that we do not **record**, **measure** and **consider** as factors that matter. And that is probably why we are still trying to get better at estimates. And that is also probably why the ideas like [#NoEstimates](http://noestimatesbook.com/) make sense and are getting popular.

**A few thoughts on [#NoEstimates](http://noestimatesbook.com/) first**

At [Agile Testing Days](http://www.agiletestingdays.com/session/noestimates-2/) 2016 conference, [Vasco Duarte](https://twitter.com/duarte_vasco) made an interesting keynote around #NoEstimates. I admit, I do feel bit brainwashed by his ideas but I believe that NoEstimates is not about “not estimating at all”. It’s about doing estimates sensibly and without blindly following the tools that are being widely practiced. 

And, in my opinion there is still some way to go till industry understands and starts practicing the key idea behind NoEstimates. Does that mean we should stop estimating right now and wait for an entire industry to on board with it? Absolutely not! 

By the time this idea develops further, I think we should continue to make efforts towards doing better estimates. After all, the fact is that business needs some date to baseline their business plans with and I find it totally reasonable. 

**What’s wrong with how we currently estimate?**

I think the problem is not just with how we estimate (story points, T-shirt sizes for example) but also with what all we measure, how we measure and what we take into account from all those measurements.

I strongly feel that there is cause and effect relationship between things we measure and our estimations based on those. If we do not measure what all matters, our estimations are likely to be flawed. And honestly, it’s high time that our industry stops measuring things that are easy (and cheap) to measure rather than those that matter but are difficult to measure.

**What are those things that (also) contribute to poor estimates? **

I can only talk about things that I have seen making an impact in my experience but I feel they can be very much present in your project environments too. Generally, these are short-lived impediments/side-tasks that we forget to **record**, **measure** and **consider **such as** :**

 	- Supporting changes by cross-functional teams
 	- Supporting changes/recommendations by architects or infra team
 	- Technical Debts
 	- Unplanned bug fixes
 	- Unplanned Functional/Technical investigations
 	- Discussions with other teams to solve certain problems or derive solutions

It’s not that we totally ignore the efforts spent on all of the above but typically those cards remain on the dashboard only for the duration of the sprint and then are thrown in dustbin when sprint is over. What if we start recording, measuring and considering them for future references? Would it not help? Where is the problem if yes? 

**Where is the problem? **

The problem, in the way I see it is that, there aren’t enough techniques that would help people identify what to measure that matters and how to measure it. In order to measure things, first we need a mechanism to observe them, and record those observations in order to measure them. I feel that for a project-team as a whole, we currently don’t have any effective mechanism to address this. This same problem had been haunting testing community badly (and caused great damage too) but I’m glad that in the form of [Session Based Testing](https://en.wikipedia.org/wiki/Session-based_testing) (and [Management](http://www.satisfice.com/sbtm/)) the community found a sensible way to do it right. 

Hey, but that’s just about testing and test management. What about measuring things (like above) equally effectively for the work that programmers do? After all, estimations are for and from whole team (and not just programmers or testers alone) unless context demands it to be otherwise. 

**Thinking about the solution**

I am wondering, what if we extend the key idea of Session Based Testing to programming as well? Yes, something like Session Based Programming?

If you are not from testing background and don’t know about [SBT(M)](http://www.satisfice.com/sbtm/) then I encourage you to read about it first. If you are a tester and still don’t know it yet then please do yourself a favour and read it NOW!

Well, what do I really mean by Session Based Programming? Here is my proposal:

1. Development to be done in focused, un-interrupted and time-boxed ‘programming sessions’, typically of the length of 30 mins or 45 mins (short sessions) to of 80 mins or 90 mins (long sessions).

2. The way testers define mission and create charters for their test sessions (in SBT space), programmers may pick stories or tasks and can work on them in time-boxed way.

​3. Typically, testers perform different types of session in SBT such as Analysis session, Survey session, PCO session, Deep testing session etc. Similarly, programmers may also classify the type of session they would be working on. Right off the top of the head, I would propose the session types like below :

These types can vary from project to project. (May be you think of new ones and let me know too?)​

4. Keep the record of actual time spent on what type of session with challenges faced if any and store them to some central location. 

**And how do we estimate with these? **

Once programmers spend enough time working in this way, over the period of time, they are most likely to develop realistic understanding of how many sessions of what type are likely to be needed to complete some story or task. This is because it is going to be based on actual experience and by keeping the actual time spent on so and so type of session in mind. 

Let me give a small example. Assume that for some XYZ story, particular complex feature in your application roughly requires some back-end programming efforts, some front-end changes and testing. A programmer (and tester) who has spent enough time working on respective area in Session Based way may come up with estimates like:

BE programmer: 3 short back-end coding sessions
FE programmer: 1 long FE+BE pair programming session
Tester: 1 short Analysis and 1 long deep testing sessions 

Assuming that short session in your team corresponds to 30 mins of time and long session to 80 mins then by calculating and combining above inputs, we can estimate the story XYZ to be taking roughly 280 ( 90+80+30+80) mins of work.

But wait, assume that historic record of time spent by team on Unplanned activities sessions, Bug fixing sessions, Deployment hiccups per sprint (of 10 stories on average) amounts to be around 200 mins (that is 20 mins for one story) . I would add this as buffer to initial estimate of 280 mins and would count the final one as 280+20=300 mins.

What is the benefit?

I think there are more than just one such as:
​

 	- The first one being your estimates are likely to be better if not accurate, for the fact that they would be based on actual time spent on different sort of sessions (that also involve complexity). This is in contrast to popular methods where estimations are generally made based on feelings, rough ideas and perceived complexities. 
 	- Since your estimations are done in the form of “number of sessions” (and not Story-points or T-shirt sizes), finding out approximate **time** to be taken is relatively easy and reliable as compared to standards methods of estimation where we don’t necessarily estimate in time required and the relationship of that measure with time is hard to establish (rather not recommended). 
 	- The idea of classifying the work in different types of sessions would force us to consider those types while planning the sprint itself instead of realising and considering them at latter stage and re-estimating the efforts. 
 	- Focused, time-boxed and uninterrupted programming sessions can certainly boost productivity
 	- When otherwise overlooked things are measured, recorded and taken into consideration then Retrospective meetings in particular can be more productive and Team Leads or POs might get deeper insights into what action needs to be taken to overcome those short-lived but repetitive impediments. 

**I’m a tester but what makes me so concerned about programmers?**

I feel that testing community has mostly been at receiving end whenever some new and shiny, cool thing happens (e.g. DevOps) and they are usually left to figure out how to “fit in”. The efforts testers spend on these “fitting in” attempts are usually so high that they hardly get to contribute to the advancements beyond their own craft. 

If testers are to evaluate and to contribute to software quality, then they should also evaluate and contribute to the quality of processes that affect them (and everyone else). Session Based Programming is my humble attempt to accomplish that.

I look forward to know how you find it. Feedback and criticism welcome 🙂

[On side note, I presented this idea in my Lightning Talks at [Agile Testing Days](http://www.agiletestingdays.com/) conference- 2016 and got some good feedback, especially from [Janet Gregory](http://janetgregory.ca/). We discussed to work on it together to take it further and I would like to thank Janet for encouraging me to do so.]