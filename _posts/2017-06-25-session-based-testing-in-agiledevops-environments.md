---
title: "Session Based Testing in Agile/DevOps Environments"
date: 2017-06-25 21:11:21 +0530
categories: [Agile, Devops, Testing]
---

![Session Based Testing in Agile/DevOps](/assets/img/posts/session-based-testing-agile-devops.webp)
​During my ET/SBTM workshops, I have been often asked if it is possible to perform Session Based Testing in typical Agile/DevOps environments.

I think if tester knows how to perform SBT (especially with different session types), there should be no trouble in doing it regardless of the development methodology their team follows. (If you are unaware of typical session types in SBTM, then I recommend you to checkout this [informative series](https://simonsaysnomore.wordpress.com/2014/08/19/session-based-test-session-reports/) by my friend Simon ‘Peter’ Schrijver.) However, I understand that probably, the fast paced way of working through sprints, shipping small chunks of software regularly, keeps everyone mainly focused around achieving the sprint goal. And for testers, this often means focusing only on ‘acceptance criteria’ and moving on to the next ticket, which is waiting to be tested and deployed.  And that might force some testers to just forget every awesome technique they know and run behind getting “the stuff done”.

If you are a tester (sorry, Agile Tester) stuck in such situation and feel bad about it, then this post is for you. For a while, I too was stuck in similar situation. Not that I was not getting to perform ET in SBTM way, but I constantly felt something was missing and that there was still more I could do. A couple of important things were getting skipped off my typical sessions, and all I could do was procrastinate them. And that was bad, very bad! (yeh)

When I was done with feeling guilty about it, here is what I did (and I strongly recommend you too try it out). I created some more session types for myself some of which I perform twice a week and some I perform daily. And they have been helping me greatly so far. Well, what are they?

**1. Critical Thinking Session **

I know, a good tester should think critically at every possible occasion. But there is no harm if you dedicate a special slot for it. How often do agile testers spend time on reading through backlog and preparing their notes in advance so that they know what to ask, know what extra information they would need for certain ticket or prepare a risk list associated with some ticket, to make everyone aware of it before it’s too late?

A dedicated ‘Critical Thinking’ session aims to solve this problem.  Schedule at-least two of such sessions, one before beginning of new sprint and one before your feedback/refining sessions so that you spend enough time for ‘critically thinking’ about stuff that would be soon on your plate. The sooner you prepare yourself with it, the better you will be able to shape your further sessions around actual testing of those items.

Medium sessions of roughly 60 minutes works great for me. Sometimes a short session of 45 mins is enough. The more you practice with Critical Thinking sessions and the more time you spend with applications you test, I guess you will eventually need lesser time for CT sessions.

In case you are wondering what I really mean by “Critically Thinking” about backlog items then please checkout “Mary Had A Little Lamb” heuristic by Jerry Weinberg or “Huh?Really?So?” by James Bach.

**2. Monitoring Session **

Monitoring production logs especially after deployments has benefits of its own.  And if tester does it regularly then there is a lot they can discover through those logs.

If as a tester, you are not yet doing production deployments then I suggest you start doing it and make sure to check production logs (or logs on other environments for that matter). If for some reason, you do not own deployments then try to spend at-least one short session for monitoring your application’s production logs, every day. That’s what I mean by “Monitoring session”.

Because of such dedicated monitoring sessions, I have come across some elusive bugs that were hard to catch on testing environment. Production logs are also very interesting means to learn about different ways in which you can test your application against disfavored use or extreme use (refer [HTSM by James Bach](http://www.satisfice.com/tools/htsm.pdf) – SFDIPOT – Operations). Not only that, it can also help you identify some illusive integration level bugs which might not be caught easily otherwise.

Monitoring sessions can also help you identify technical bugs, errors or warnings, which might not be directly affecting the end user but still warrant attention and fixing. It’s hard to identify such issues in regular functional testing which usually has big scope of its own.

**3. Bug-visit Session **

This session is about visiting the bugs in backlog and going through them carefully. Sometimes, over the period of time, some bugs become irrelevant or can also become important to be fixed on priority. Revisiting those bugs helps take appropriate action on time.

If there are bugs logged by other teams or customer care team for example, then they can also serve as a great ‘test ideas’ that can be extended to other features of application. Information gathered through such bug-visit sessions can help you create your own risk-list or project specific heuristic (I have explained that in detail with [HEEENA](http://www.talesoftesting.com/blog/heeena-a-heuristic-to-create-your-project-specific-heuristic)).

**4. Test for Testability Session**

I can’t stress enough on importance of this session, especially in this changing era of Software Development. One of the key role a skilled tester can play in modern software development is of “advocate of testability”. Checkout this heuristic for [Software Testability](http://www.satisfice.com/tools/testability.pdf) by James Bach.  Once you understand the dynamics of testability you will realise that the sooner you care for it (and advice where needed) the better testable product your team will create. If I am to give you an example, please check “[stats for nerds](http://tubularinsights.com/youtube-stats-for-nerds/)” on youtube videos you watch. Would such information not help you if your product starts storing such information, that you as a tester can access easily and shape your tests based on that?

I suggest you create the checklist for **Intrinsic Testability** in particular and test your design right from the beginning against it. Please dedicate a compulsory session (short should be good to begin with) for testability even before you get the build for testing against acceptance criteria. In fact, you could also pair with programmer or PO when they work on user stories that will latter come to you for independent testing. This in tern will help you as a tester to better test the product for session/charter you care for (and you won’t get lost in figuring things out to help you test better).

So, that’s about four additional session types I have created for myself to do even more effective SBTM in agile environment. I am finding them very useful and hope you too will benefit from them.

Feel free to get in touch if you have any questions or would like to discuss it further.

Happy Testing!

​Header image credit – blog.xebia.fr