---
title: "Interviewing Programmers for Quality Mindset"
date: 2017-10-29 07:00:00 +0530
categories: [Agile, Career]
image: "/assets/img/posts/lalit-meet-the-speaker.jpeg"
---

Lately, I happened to have an interesting discussion with my colleague [Dirk Meißner](https://www.xing.com/profile/Dirk_Meissner33/cv) on whether programmers should have reasonable understanding of testing or not. A lot has been talked and written about how testers need to be great with their technical skills so that they can contribute effectively and remain valuable. Sure, that’s helpful and I too insist that it’s high time that testers get over with their traditional way of working (and thinking). However, what surprises me is that there is not enough awareness or enough discussions happening around programmers learning to understand testing to amplify their effectiveness.**Does it matter? Why? **

It absolutely does. At least now, if it did not before. “[Whole Team Testing](https://www.agilealliance.org/resources/sessions/whole-team-testing/)” is new cool (again) especially in DevOps contexts. And it has it’s own reasons to be that way.

Let me explain. Agile teams typically have one tester dedicatedly looking after testing and related activities in team. This tester is usually busy testing (and automating often) stories for each sprint with primary focus on acceptance criteria. If the tester is “cool kid” then they go over the board and test things beyond acceptance criteria too. Cool! Let’s park this thought here for a moment. Okay?

James Bach, in his interesting article “[**Seven Kinds of Testers**](http://www.satisfice.com/blog/archives/893)“ beautifully explains the key patterns surrounding testing styles and how testers typically fit into one pattern or the other or combination of more some times (or checkout this thought-provoking [**tweet series**](https://twitter.com/michaelbolton/status/924371675466039296) by Michael Bolton).  In over eight years of hands-on experience of testing, I have found myself to be of one kind (or maximum two) at a time and by the time I wish to change my hat (or style) it is usually almost the time to deploy the feature in production. Pity!

The point is, there is limit on how much versatile a tester can be in limited period of time for each story they test. Sure, it’s not impossible but I would say it’s not very easy either, given the time constraints. Now, imagine that we add “programmers” from team as other kinds of tester (based on their skills, expertise and experiences) working on same story. Do you not think it will most likely add more coverage to the quality of that feature, without having to spend really additional time on it? Do you not think that testing wisdom of a programmer would help tester and the team to ship quality product? I’m sure, now you do!

When I say programmers should contribute to testing, it does not have to be only in a way that they will need to test the software like testers do. Even if they develop the required mindset, it’s already a good start. Indeed it will be great if they can test it but I feel that if they could at-least understand modern testing, it will greatly benefit the project teams.

How exactly programmers can learn to test and start off with it, or how testers can help them to onboard with testing is another topic. It requires a dedicated post (more on that later).

This post is about identifying programmers with testing mindset or skills that can help them test better, while you interview them. I recommend watching out for these skills/traits in interview:

**1. Quest for Context**

*The scholar [**John von Neumann**](https://en.wikipedia.org/wiki/John_von_Neumann) once said, “There’s no sense being exact about something if you don’t even know what you’re talking about.” In a world that is growing increasingly dependent on highly complex, computer-based systems, the importance of defining what you want to make before making it — that is, knowing what you’re talking about — cannot be stressed enough. *([**Exploring Requirements: Quality before Design**](https://www.amazon.com/Exploring-Requirements-Quality-Before-Design/dp/0932633137) by [**Weinberg**](http://www.geraldmweinberg.com/Site/Home.html) & [**Gause**](https://www.linkedin.com/in/donald-c-gause-89211947/)).

Developing software is not just about writing a program that will do the stuff but it is more about building a product that your customer would like to use. In past, I have come across programmers who were excellent coders but failed to care enough about purpose of the program they used to write. I rarely see programmers questioning the user story beyond acceptance criteria and technical implementations if any (unfortunately, it’s not very different for majority of testers either).

If I were to hire a programmer, I would expect him to ask [**Context Revealing questions.**](http://www.developsense.com/blog/2010/11/context-free-questions-for-testing/) By that, I don’t mean just questioning the business value of the user-story. There are things beyond that which matter. What if we find out that other team has worked on similar solution before? What if we could re-use some components developed by other teams?  What happens when particular feature development requires specific technology expertise and team does not have it? What happens when stakeholders’ understanding of technical details defer from engineering team’s? What if implementation of some solution requires tools not available with team or required access levels for that matter?

Sure, one can eventually find these things out when they start working on the ticket but what’s the point in findings things with accident and when it’s already late?

Programming interviews typically include coding challenge that typically gets assessed for candidate’s technical skills, familiarity with known technological issues, understanding of best programming practices, problem solving skills etc. which are indeed important. However, I am yet to see a programmer being assessed for the kind of questions they asked before jumping on to the coding challenge itself.  See if they are questioning the very purpose of challenge, see if they question the business value, check if they ask about other elements of [**Project Environment**](http://www.satisfice.com/tools/htsm.pdf) and [**Product Elements**](http://www.satisfice.com/tools/htsm.pdf) for that matter.  And, please check if they ask questions about testing and [**Quality Criteria**](http://www.satisfice.com/tools/htsm.pdf) if nothing else. Most of the programmers I got to interview usually assumed that that there will be a tester in team who will QA their code. They just have to write the code and throw it in tester’s bucket. You better watch for such kind if your team does not have a tester.

Just like testing, good software development should be treated like an intellectual activity. The better one understands it the more ways one can contribute to product quality. And it all begins with asking questions.

​**2. Interactional Expertise **

If you are unfamiliar with the idea of [**Interactional Expertise**](https://en.wikipedia.org/wiki/Interactional_expertise), I suggest you start from understanding it first. Even better if you could read [**Tacit and Explicit Knowledge**](http://press.uchicago.edu/ucp/books/book/chicago/T/bo8461024.html) by Harry Collins.  I personally found it to be very useful learning when I was introduced to it by my friend [**Iain McCowatt**](https://www.linkedin.com/in/imccowatt/).

​The purpose of mentioning Interactional Expertise as a skill here is that, I find it to be very important skill when it comes to have technical discussions with non-technical people. Or, even when it is about having meaningful technical discussions in short period of time.

Bringing up technical topic for discussion in planning meetings or grooming/estimation meetings is usually like opening the Pandora’s box. Over the years, I have been a part of deep discussions in meetings with only conclusion of carrying them to next meeting or scheduling separate meeting for that. Then again, special meetings for explaining those technical things to non-technical people were required. Does that not sound familiar to you?

I feel that spending so much time on deep discussions very often is unnecessary and it can be significantly controlled if all of us (not just programmers or testers) learn the skill of explaining things in short (and to the point) when needed without losing the substance of it or compromising with the impact an elaborated version would make. Same goes with explaining technical things to non-technical people. As techies, we can’t expect the whole world to understand the language we speak (it would be nice if that happens though) but we can make things simple by learning the art of explaining those to other in language and context they would understand better.

Added advantage would be when you onboard new members in team. Regardless of what role they are hired for, person’s IE skills would help them onboard much better and the skill will definitely help for better collaboration and communication. In fact, when testers and programmers both have great interactional expertise then sessions like pair testing or programming will be super productive. Imagine what value it can add for Mob Programming and Mob Testing sessions. I have worked with some programmers who were master of explaining technical things to non-technical members of team as if they were putting a child to sleep by telling a story. Short, sweet and yet satisfying. That’s what I mean by Interactional Expertise.

Next time when you interview a programmer, look for these. It will help you. When I interview testers for it, I usually ask them to explain some technical concept in 50 words for example and again same concept in 100 words. It helps me analyse how good (or bad) they are with their Interactional Expertise. Asking programmers to write a technical bug report or user story can also be helpful trick to evaluate them for their IE.
​
​**3. Understanding of Testability **

May be I am wrong about it, but I honestly feel our industry still lacks required seriousness (and awareness) for building testable products. This is not just about programmers being unaware of it but even testers.

The only times I hear of the word “test” in programmer interviews are when they talk about their unit tests or TDD or automated tests at the max. And it’s a pity!

Building testable products is an important part of software development and it is important that programmers understand how to bake testability right from the beginning. Sure, skilled testers can certainly be advocates for testability but it won’t hurt if programmers too understand what it means to them and how they can contribute to it.

While interviewing programmer, I suggest you pay special attention to their solution if that demonstrates at-least few aspects of **Intrinsic Testability** as explained in ​[**Heuristics of Software Testability**](http://www.satisfice.com/tools/testability.pdf) by James Bach. If not, at-least make an attempt to discuss other aspects of software testability (listed in the heuristics) with candidate in general and gauge their fitness for your requirement.

For sure, the skills mentioned above are equally important for testers too but since “Whole Team Testing” thing is picking up, I wanted to make it explicit for traditional non-testers. Next time when you interview a programmer, please try and see if it helps.

If we need technical testers, we also need programmers who understand testing. And that is reasonable to ask for, isn’t it?

Oh and by the way, I will be touching on some of the related topics in my talk for [**Online Testing Conference**](http://www.onlinetestconf.com/?utm_source=speaker&utm_medium=share&utm_content=Lalit). Feel free to join if the topic interests you.

[![Lalit - Meet the Speaker](/assets/img/posts/lalit-meet-the-speaker.jpeg)](http://www.onlinetestconf.com/register/?utm_source=speaker&utm_medium=share&utm_content=Lalit)