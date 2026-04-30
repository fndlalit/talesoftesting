---
title: "Cake, Coffee and some POT"
date: 2017-05-28 13:08:07 +0530
categories: [Agile, Devops]
---

Before some of you start freaking out, let me make this clear – no, it’s not the pot some of you might be thinking of 🙂. It’s an abbreviation of “Problem on Table”, an activity we have recently started doing at XING AG for its testers.

As facilitator, I have experienced the benefits of POT method of problem sharing (and solving). I was first introduced with the idea at ITB tester meet-ups I participated in Pune/Mumbai and in order to facilitate such exchange for testers at XING, we decided to give it a try with some twist. And guess what? It worked really well!

**How does it work?**

The key idea of POT session is that testers come together and share their testing problems.  This is done in order to get support from fellow testers who might have faced similar problems before or you find more testers facing similar problems and then work together to solve them.

The format of POT sessions I did in past used to turn out chaotic soon, because of lack of moderator control over discussions, too many topics being discussed at a time etc.  And that sometimes used to confuse the problem presenter instead of getting solutions to the problems they shared.
**Presenting “POT – the Lean Coffee style”**

To make the exchange less chaotic and inclusive for everyone, we decided to do it in Lean Coffee way. And boy, it did wonders!

If you are aware of Lean Coffee and now POT then it should be rather easy to guess the format.

Set-up notes for facilitators:

 	- Find nice café (or any place for that matter) where people can sit back, relax and discuss things freely (optional, but works great).
 	- Create three columns on wall or table with **To Discuss**, **In Discussion** and **Discussed** (or just To Do, In Progress and Done should be good).
 	- Keep enough post-its and pens/markers handy

Here are some simple rules we followed that worked great for us:

 	- Group size of not more than 5-6 (including facilitator) on one table
 	- Each participant in the group gets to write one card around testing problem they need help with, in not more than 3 minutes
 	- Facilitator to stick all post-its in **To be Discussed** column to begin with
 	- Each members gets 2 minutes to explain their card/problem in brief
 	- Group then does dot-voting on topics after which facilitator re-organizes the cards from highest voted to lower ones.
 	- Then like typical Lean Coffee session, group discusses the topics one by one in time boxed manner and voting each time if they would like to discuss the topic further or move on to next one.
 	- I strongly recommend that facilitator (or someone else in group) makes sure to take notes of solutions discussed
 	- When there are more than 5-6 testers wanting to participate, I recommend that you make multiple groups and then share your notes latter on or you reshuffle the groups for next sessions.

And that’s it. You are ready roll!

Our first POT- Lean Coffee style session went on for two hours with five minutes break in between and I am super glad that we had some much cool stuff to discuss and everyone had some or the other idea to solve their respective problems.  That’s the power of teamwork, isn’t it?

**The key takeaways from our first session:**

In two hours of highly engaging discussions, below are some problems we discussed and the solutions we felt could help solve those. I strongly feel that many testers would face those challenges regardless of the organizations they work for and hence I am sharing the solutions we discussed, hoping that others with similar problems might find them helpful.

**Problem 1: What happens when Tester goes on vacation? **

A classic problem many Agile teams face in my opinion. So, when tester (who is generally only one person doing testing in team) goes on vacation or falls sick, the team usually suffers and tends to rely on automated tests or performs minimal testing which often results into big problem. What a tester can do to solve it? Or if I may say, what teams can do to solve this problem? Here are some ideas that have worked with some of us:

 	- Make team understand that Quality is team’s responsibility and needs to be baked in at each stage of development instead of relying on some Quality inspector to inform about problems towards end of it. But that’s easier said than done, right? Worry not. There are ways to do that.  Try WIP limits in your sprints may be? When tester is already stuck with some tickets and when rest of the team can not proceed because of WIP limit, it compels others to help tester in finishing his job so that WIP licenses could be freed for further work. May be rest of the team won’t be able to test as meticulously and productively as one skilled tester would, this will still make them used to the process, philosophy and mind-set. And when tester is on vacation or falls sick all of sudden, team will have something useful to do instead of panicking or freezing in headlights.
 	- Other cool way to on-board non-testers to work as tester in emergency would be to try ‘pair testing’ sessions with programmers one by one or to do ‘mob testing’ sessions as a team. Each of them has benefits of their own. And from personal experience I see value in them.
 	- Some other ideas would be to create hand-over documents, test plans, test-idea mind-maps, videos and confluence pages around “How to test it” in advance.

**Problem 2: How to manage integration testing with different teams/apps?**

If the app your team builds is just one part of several applications working together for your one business product as a whole, it often becomes challenging to plan out and maintain hassle-free deliveries throughout. And end-to-end testing becomes even more challenging under some circumstances.

Different teams are likely to have different notion of quality, different development methodologies, different business plans and thus, naturally different release plans. Things become chaotic when testers are left alone to solve such problems, or when such problems are identified very late in development of some feature with rigid deadline.

And who else can understand such problems any better than fellow tester from other team? Do you see some solution there? We did and I believe it helps. Here are some ways to facilitate that:

 	- Meet testers from other teams over coffee or so and have an exchange around what feature they are changing soon and seek to understand what those changes mean to you and your test strategy. Of course announcing such things on chat-rooms or confluence pages could help, but we felt that having in-person discussions would be more effective.
 	- Create combined test strategy that takes into account the release plans of both teams, impact analysis of changes to be made, sharing of testing scope or perhaps building some reusable components for each other? (like helpful scripts, automated tests, test data set-up etc.)
 	- To facilitate the cross-functional knowledge pairing sessions with testers from other teams, or asking/offering peer review on your/their tests/automated scripts, pull requests could be helpful. All such reviews do not have to be done by programmers as it typically happens. If testers start taking part in those, we feel it would benefit everyone.
 	- Some sort of mutual contract or protocol can also be established between testers from different teams who usually test the apps that have high integration dependencies. I would call it as a take-away from informal meetings or pairing sessions etc.
 	- Early involvement of testers in feature kick-off or product planning can also help POs or Team Leads to identify such dependencies in advance and consider those in their planning. We feel, tester should ask for such involvement if they are not involved already. POs/TLs would definitely love you for throwing light on potential problems of future.

Some of the other issues we discussed were around pushing for bug-fixing, fixing high-bug-tolerance problem of agile teams, common pitfalls of agile testing, what real agile testing should look like etc. One of the suggestions from our experienced tester [Dirk Meißner](https://www.xing.com/profile/Dirk_Meissner33) was to hire programmers who take testing seriously and have quality mindset. I feel that’s very good approach. Precaution is always better than cure, isn’t it?

So that was about some key things we discussed in our first POT-Lean Coffee style meet-up. And we are already excited about the next one. How about creating one in your organization and sharing your learning with us, just like I did? Let there be some coffee, some delicious cake and of course some Problems on Table. Enjoy!

Header image credit – wall.alphacoders.com