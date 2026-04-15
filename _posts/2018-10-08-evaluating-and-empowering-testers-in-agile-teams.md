---
title: "Evaluating and Empowering Testers in Agile Teams"
date: 2018-10-08 22:00:00 +0530
categories: [Agile, Career, Devops, Testing]
---

![](https://talesoftesting.com/wp-content/uploads/2021/11/evaluation.jpeg)

**​Disclaimer:** The purpose** of this blog is not to undermine the importance of automation skills for testers but rather to highlight the lack of awareness in our industry for tester’s usefulness in teams beyond typical testing and automation tasks. **​Recently, I was invited to conduct a workshop around “Whole Team Testing” at Test Leadership Congress in New York. Participating in this conference has been a great experience, especially because I truly believe in the need for conferences dedicated to testing leadership and career path for testers in changing era.

The discussions I had there with fellow testers, managers, and directors of engineering/testing were interesting. Well, not only interesting but insightful and with lots of ideas, concerns, observations to ponder upon. Out of the things we discussed, what held my attention the most was the growing concern of evaluation of testers in Agile teams. The evaluation can be for hiring or for their overall performance in the team.

**What is the problem exactly?**

If you analyze the trend from [State of Testing](http://qablog.practitest.com/wp-content/uploads/2018/07/2018_state_of_testing_report_1.2.pdf) report, it is evident that with increasing Agile adoption, centralized testing units are mostly getting dissolved and testers are now reporting to Dev/Team leads. With this change of structure, hiring new testers and evaluating those in teams naturally becomes the responsibility of the Dev/Team leads. And this is where things start to get interesting. How? Let’s take a look:
​
- Dev leads are usually excellent programmers with high passion and inclination towards the typical programmer mindset. And this is very natural.- Neither all of the leads come with prior experience of hands-on testing nor all are well versed with testing mindset and philosophy which is the key differentiator between testers and programmers. The way programming excellence comes with a deep understanding of programming concepts and ample hands-on experience of coding, it is quite natural that in order to understand testing better (so as to evaluate people for testing skills) one has to have equivalent expertise or at-least deep understanding of the subject. And this is something our industry is still lacking, unfortunately.- But despite this, teams still need testers and they must be hired and evaluated. What happens in such situations? Testers get evaluated based on the scale and criteria, that hiring managers (programmers at heart) are most comfortable with.  Yes, read that as automation and programming skills. This is quite natural, mostly happens unconsciously and I won’t blame it on them entirely.
But this situation is dragging us into a bigger problem. *We are giving too much importance to things that are just a part of a big scheme of things that matter and contribute to software quality and teams’ overall ability to ship quality software, faster and frequently. *

*Of course, automation skills and other technical skills are helpful, rather important I would say. But that has become a norm now and what we really need at this point in time are tools to see beyond this norm.* If we want excellent testers in the team who can really add value to software quality, it’s high time that hiring managers come out of their obsession with hiring testers based on the norms that they can most comfortably evaluate. Please, it is not about what we are most comfortable with but what the Agile team really needs from a tester to ship quality software.

Heavy emphasis on technical skills for testers is not my big concern, but lack of awareness around other things that testers must get evaluated against concerns me the most.  The purpose of this article is to highlight some of those areas (beyond typical technical skills) that I think managers/leads may want to consider while hiring new testers or evaluating those in their teams.

**Why do we need testers in the first place?**

One may argue that in an era of AI and advanced automation where every **check** can be easily automated, why do we need human testers at all? That’s an interesting argument  and before I explain why we are talking about it,  I want you to have a look over the diagram below:
![](https://talesoftesting.com/wp-content/uploads/2021/11/Feedback-effects.png) 
The diagram represents a system that we as a team operate into. I created it based on my experience as a tester so far and by interviewing some programmers I have closely worked with. Looking at a bunch of things mentioned there, you can figure out what all can happen (rather typically happens) when a tester in the team is not available. If you read the diagram carefully, you will notice that the impact on finding and reporting bugs is just one segment that gets highlighted when the tester is missing in the team. Impact on writing new tests or automating them is another segment. But is that all you need testers for in a team? Certainly not!

The purpose of having testers in the team is way beyond finding bugs, writing tests, or automated scripts for that matter.    If utilized to their full potential, testers in the team can very well serve as a mode to protect your system from running into collapse or explosion mode (please read more about that in “How Software is Built” by Jerry Weinberg). How? It’s simple. By providing system-related feedback to the controller which is typically the team lead or test manager in a typical team set-up. The better you utilize testers for their abilities the better feedback you get from them which in turn can help you command better control over your system and protect it from collapse/explosion.  You need a tester in the team to provide you with information that you as a stakeholder can use for making better decisions.

And when I say feedback, it can be anything from information about bugs, risks highlighting, asking context revealing questions, questioning user stories or decisions made, finding out historical data, highlighting third-party dependencies, sharing news about decisions made by cross-functional teams, collaborating with other disciplines to create valuable assets, their observation around team dynamics, their predictions about possible failures and so on. And if you are lucky, they can also tell you some great things about the quality of your product.

The point is, testers in your team can add far more value beyond finding bugs if you allow them to contribute beyond their typical role. If not, you can always empower them to do so. Here are a couple of things that in my experience testers can contribute to and against which you could evaluate them (for hiring or performance reviews etc):

**1. Primary analyzer of production logs and alerts **

Production deployments are typically done by programmers who then closely follow the logs to see if there are any obvious issues created by the latest build. Consider handing over this responsibility to testers. It is likely to serve multiple purposes:
- Time spent on back and forth of sending build for testing and deployment can be greatly reduced. Once the tester is done with their testing, they can directly promote the build for deployment.- Participating in the deployment process can help the tester understand the underlying infrastructure and can offer a better technical overview of how those dependencies can affect end-to-end testing and delivery of your product. This understanding can also help them better analyze the logs and use those for technical investigation of observations made.- Over the period of time when enough insights are acquired, using their sharp observation skills, familiarity with known issues, and ability to quickly analyze the gaps, testers can help identify the root cause of problems, functional and business impact as they read the logs and draw inferences from those.- Using the failures and errors via production logs, testers can derive more tests for the future and also identify risk areas that were hidden until a given point in time.- Participating in production deployments and monitoring can certainly foster better collaboration and pairing between programmer and testers which has benefits of its own.
**2. Enhancers of your product’s coverage for quality**

It has very little value if the tester in your team just sticks with the usual acceptance criteria for the ticket and automates the stuff for you to top it. The real value a skilled tester can add is when they question the very product coverage you have in place and help your team see elements of the product that matter from quality aspects.

A lot of elements matter when it comes to your product’s quality. Functional acceptance criteria are just a tiny part of it. A skilled tester would know about these elements and they would educate the team about the same.

Check out [SFDIPOT](http://www.testingeducation.org/course_notes/bach_james/cm_2002_rapidsoftwaretesting/rapidsoftwaretesting_10_heuristic_test_strategy_model.pdf) from [HTSM](http://www.testingeducation.org/course_notes/bach_james/cm_2002_rapidsoftwaretesting/rapidsoftwaretesting_10_heuristic_test_strategy_model.pdf) by James Bach or simply have a look on mindmap below (thanks to [Albert Gareev](http://automation-beyond.com/wp/wp-content/uploads/2015/02/SFDiPOT.png))
![](https://talesoftesting.com/wp-content/uploads/2021/11/SFDIPOT.png) 
**3. Advocates for Testability **Testability is one of the key areas I would expect skilled testers in my team to help programmers and designers get it right.  A skilled tester would know what makes a product testable, how to evaluate it for testability, and also advocate the team as to where and how they can improve it. Nothing beats the pleasure of testing a better testable product.

Here is a [heuristic for testability](http://www.satisfice.com/tools/testability.pdf) if that makes you curious. Out of the various types of testability mentioned there, I would expect the tester to at least know **Intrinsic Testability **and how to help their team improve it.
![](https://talesoftesting.com/wp-content/uploads/2021/11/Testability.png)
**4. Better allies for UX peeps**Ever wondered what would happen if System Thinking meets Design Thinking? I firmly believe that challenges faced by testers and UX professionals are more or less the same when it comes to ensuring better quality and better user experience.

A regular and close exchange between these two disciplines has tremendous potential to create a better user experience with enhanced product quality which I would call “[Quality Experience](https://talesoftesting.com/quality-experienceqx-co-creating-quality-experience-for-everyone-associated-with-the-product/)”. If a UX designer comes with one best solution for some product problem, a skilled tester with their insights, product knowledge, awareness around cross-functional dependencies can point out a variety of ways in which it may fail. This does not mean a tester has to criticize UX solutions as such but early collaboration and exchange between two can help avoid lots of unnecessary research and rework.

On other hand, testers can borrow realistic information from UX’s research which can help them design tests that matter and prevent themselves from straying into unwanted scope. Testers can borrow statistical data or interaction/persona-based information from UX that can help them shape better scope for their tests. Well, this is indeed an interesting topic and deserves deep dive. I will stop here on this one for now.

A skilled tester would make this collaboration happen and would bring out the best from both worlds.

**5. Friend in need for marketing and user care **

This is another area of collaboration where skilled testers can add great value to solve the team’s problems beyond finding bugs. I have listed some of the possibilities where testers can help user care and get benefit in return and I believe the same applies to their collaboration with marketing teams:
![](https://talesoftesting.com/wp-content/uploads/2021/11/User-Care.png) 
**6. Alert mechanism when the system is on the verge of collapse **

Well, this is a bit tricky but I would mention it anyway. By nature of their work, skilled testers can use their sharp observation skills to observe and understand people, situations, and events around them and can draw inferences that can help identify potential risks, before it is too late. The retrospective meeting is a great place for skilled testers to raise flags for potential issues surrounding team dynamics or people issues they observed, in a constructive way of course which is where their communication skills can come in handy.

Testers are usually in touch with fellow testers in the organization from where they get information around what other teams are working on, their future plans, blocking issues, etc and this information can be very well used to analyze the impact on their respective team’s road-map, work in progress or work items that share dependencies with other teams.

A tester who is skilled enough to foster network and relations across teams can certainly help bypass blockages when the team needs it most.
​
So, those are some aspects in my opinion and experience, a skilled tester can contribute value to project team beyond their traditional tasks.

If you are to a hire new tester or would like to fairly evaluate/mentor a tester in your team, I would suggest giving these ideas some consideration. It’s high time that we look at a tester as someone beyond bug-finder. They can do wonders for your team and can help to accelerate the shipping of quality products if allowed to use their full potential.

​I shared what I think can be helpful. Feel free to chip in your ideas ….