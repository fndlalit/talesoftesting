---
title: "#20DaysofTesting at XING - catching up﻿"
date: 2016-09-23 09:20:42 +0530
categories: [Uncategorized]
---

[![Picture](https://www.talesoftesting.com/uploads/3/9/4/5/39452505/lunch_orig.jpg)](https://www.talesoftesting.com/uploads/3/9/4/5/39452505/lunch_orig.jpg) 

Hmm…. I was sort of in a cave after day 5th and now it’s action time for me again. 

Not that I was totally out of the challenge but could not manage to blog about it. So… here is the list of tasks on my plate and what I did about them (u**pdates for the pending tasks are in brown)**

**Day 6. PAIR WITH SOMEONE OUTSIDE YOUR BUSINESS UNIT OR OUTSIDE QA**

I paired with a free-lance programmer who was helping us with our ongoing project on-the fly. Time was critical and he needed someone with enough knowledge about stuff he was working on. We paired up to develop it and test it on the fly. 

I used the [MIPing technique ](http://www.satisfice.com/blog/archives/97)(Mention in Passing) to report my bugs/findings and re-tested the things as he kept on fixing them. It was indeed fun pairing with a programmer and contributing right from the coding phase for new feature getting built. We benefited from each other’s expertise. My programmer counterpart got the on-boarding that he needed and also learned about the dependencies we had to resolve. I got benefited by watching closely how he quickly developed the components, wrote his unit tests and ways to resolve conflicts. 

**Day 7. GIVE SOMEONE POSITIVE FEEDBACK OUTSIDE OF QA**

The last few weeks have been crazy for us at work since we have been working on some serious stuff and the fun part is the complexity of the solution we have. At times, we can’t escape from dealing with the complexities of the software/projects and this whole thing makes testing and bug-investigations even more challenging. The reasons are obvious. The interfaces, dependencies, various states of the systems involved, pre-requisites for use cases and schedule, new features added , subsequent impact and regression add a lot more to already existing complexities. 

Among other things we found and fixed, we were struggling to resolve one bug which was hidden deep under the interfaces and lost in the complexities of interfaces.  Finally [Lars Schirrmeister](https://www.xing.com/profile/Lars_Schirrmeister) (our Senior Back-end Engineer) jumped in and decided to get to the root of it. 

After spending quite some hours on fixes and trials (Try — and See — If it works) he finally found the problem. And fixed it of course. But what was so special about it? It indeed was. The problem Lars identified was found out because of his own understanding of the technology, algorithms and syntaxes. The issue he found out was ‘never raised as an error or exception by the system itself’ and finding out hidden problem in a code laden with complexity, that does not show up in compilation/debugging at all is indeed an intelligent task. Good job Lars!

It’s an honour for me to be working with a such highly competent team and managers. There has always been something or the other I could mention in their admiration. This particular case is one example of it.  I’m glad that I could talk about my team with the world because of this challenge. 🙂

**Day 8. ****HAVE LUNCH TOGETHER AND POST A PICTURE**

Who else could be a better date for this day of challenge other than one from fellow participants :). It was great meeting Daniel Knott over lunch to discuss testing and this 20days challenge among other cool things . Feel free to check Daniel’s [updates](http://adventuresinqa.com/) on this challenge.  

There goes our picture together: 

**Day 9. ****AUTOMATE ONE WORKFLOW FROM ANOTHER ****BUSINESS UNIT **** (Pairing allowed, but be the driver)**

Could not mange to complete this task in time. It’s WIP though.  

**Day 10. ****PERSONAL CHOICE (Testing related, surprise us!)**

I’m conducting a workshop on [Impact Mapping](https://www.impactmapping.org/) for my colleagues, on 13th Oct. The idea is to implement the concept on team level (rather than keeping it limited to Senior Managers, Product Managers, SCRUM masters etc). 

My workshop would mostly talk about implementing IM on Story level and writing them with information, enough to build testable features with wider coverage. Won’t say it is only related to testing but it would definitely benefit testers working in Agile teams. 

**Day 11. ****LISTEN TO A TESTING PODCAST**

I listened to [DevOps and Technical](https://www.qualitestgroup.com/The-Testing-Show/devops-and-technical-testers/) Testers podcasts featuring Noah Sussman, Michael Larsen, Perze Ababa and Justin Rohrman ( yeh, all cool people 🙂 )

I feel this discussion has come on the time when testers needed it most. If you are wondering about what DevOps is and what roles testers can play in it then please consider listening to it. Highly recommend!  

**Day 12. ****PERFORM A CRAZY TEST**

Hmmm…this is my kinda topic. Well, honestly I don’t remember the last time when I did not perform a crazy test 🙂 The degree of craziness of a test might vary from a tester to tester based on what they perceive it to be.                                      

For me, a test performed with minimal knowledge about application and acting like a ‘first time user’ is equally crazy test. With minimal knowledge I mean not getting blinded by the specifications and testing things with open expectations. [Paul Holland](http://testingthoughts.com/blog/author/testthought) has written an interesting piece around it, [please do read it](http://testingthoughts.com/blog/185).   

On contrary, while testing the recent build of our product, I came across many ways to perform crazy tests with enough knowledge about software, dependencies and solution implemented. And I learned very important thing that a crazy test does not always have to be around the ‘disfavoured use’ or ‘extreme use’ of software (please check  Product Elements in [HTSM by James Bach](http://www.satisfice.com/tools/htsm.pdf)). Playing around with the configurations, states of a test data, teasing the pre-requisite states of system meant for some desired results or challenging the the implemented solution itself via variety of tests can also help uncover a lot of interesting things. Defects won’t always be the outcome here but knowing in advance how system behaves against all such adversities can help build lots of useful tests that can find hidden and illusive bugs. And it may also help to be prepared with fall-back solutions. 

It’s hard to explain without enough details but for example one can perform crazy test by trying to break the protocol/steps meant to be followed to reach certain state of the system. What happens if state 1 is left buggy and state 2 is still turned ON? What happens if one tries to enter the state 2 without fulfilling the pre-requisites from state 1 and so on…

More on that with publishable examples later… 

**Day 13.** **DOWNLOAD A MOBILE APP, FIND 5 BUGS AND SEND THE FEEDBACK TO THE CREATOR**

It’s last day today and I doubt if I would be able to make it. However, I have a try for testing recent release of IOS 10 and noticed that the spell checker wasn’t working as expected. That is, when you select the incorrectly spelled word for correction, the options that you would get would only be for formatting, copy paste etc and there was no ‘suggestions’ for the possible correct word. 

I do have some plans to test some interesting apps though…but time demands me to do something else, more important at this time 🙂

**Day 14. FIND AND SHARE A QUOTE THAT INSPIRES YOU**

There isn’t just one that inspires me. I have bunch of them in my collection. Sharing some of my favourite though

*1. Endow your will with such power that at every turn of fate it so be, That God himself asks of his slave, “What is it that pleases thee?” – Allama Iqbal 

2. Your ideal form of influence is to help people see their world more clearly and then to let them decide what to do next    – Jerry Weinberg  

3. There is no test for ALWAYS – James Bach*

**Day 15. CONNECT WITH A TESTER WHO YOU HAVEN’T PREVIOUSLY CONNECTED WITH**

Connected with Cassandra H. Leung (Tweet_Cassandra) and Abby Bangster (@a_bangser) on twitter. It’s always pleasure to connect with like minded testers. 

**Day 16. ****SUMMARISE AN ISSUE IN 140 CHARACTERS OR LESS**

*Take 1:  An “issue” can be anything that concerns the stakeholders. (Char 59 + Whitespace 9)

Take 2: The real issue is that I can’t give more details about because it is an internal thing. (Char 88 + Whitespace 17)*

**Day 17. ****FIND A USER EXPERIENCE PROBLEM**

I came across some websites that are offered in multiple languages (e.g. English and Deutsche) the image illustrations were updated in chosen language. For example if the adverts and campaigns and some “How-to”s are shown in pictures and they are only made in one language then it adds to bad user experience of other set of audience who don’t understand that language. 

**Day 18. ****SHARE YOUR FAVOURITE TESTING TOOL**

I like bunch of them meant for different purpose.  By the way testing tool for me, is any tool that assists me test better.
​ 

- I like [XMind](http://www.xmind.net/) when it comes to document my tests and note taking 
- I like [Omnibug](https://chrome.google.com/webstore/detail/omnibug/bknpehncffejahipecakbfkomebjmokl?hl=en) and [Observepoint](https://chrome.google.com/webstore/detail/observepoint-tag-debugger/daejfbkjipkgidckemjjafiomfeabemo) for pixel tracking testing
- [Postman](https://www.getpostman.com/) is my favourite when it comes to test APIs. 
- I like [iTester](http://altom.ro/itester) for performing Session Based Testing on mobile devices (Kudos to Altom team for developing this). Their SBTM tool with [Google Drive](http://altom.ro/blog/sbtm-with-itester-and-google-drive) is equally awesome 
- [qTest Explorer](https://www.qasymphony.com/testing-platform/qtest-explorer-exploratory-testing/) is also one amazing tool I like to use to document my test- sessions.
- Oh and how can I forget [Bugmagnet](https://gojko.github.io/bugmagnet/) from Gojko Adzic? It’s awesome too!

**Day 19. SAY SOMETHING NICE ABOUT THE THING YOU JUST TESTED**

We successfully rolled out a very complicated and critical release to production. Because of the nature of complexity of the solutions and new things we added on the fly, I was bit skeptical about completion of testing but I’m glad that we did manage it well and the code was robust enough to handle my all sort of crazy (and not-crazy) tests gracefully. 

**Day 20. TEST YOUR PRODUCT FOR A QUALITY CRITERIA, WHICH NORMALLY IS NOT A FOCUS IN YOUR ****BUSINESS UNIT**

I do this all the time to be honest. My checklist for Quality Criteria is pretty comprehensive and we keep adding new aspects to it when we see enough problems of the kind, to count. However, I have added some items to “Compliance” testing aspect recently which we were not doing with special focus before.