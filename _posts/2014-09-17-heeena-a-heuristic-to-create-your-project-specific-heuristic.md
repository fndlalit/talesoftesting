---
title: "HEEENA - A heuristic to create your project specific heuristic"
date: 2014-09-17 18:51:27 +0530
categories: [Uncategorized]
---

[![Picture](https://www.talesoftesting.com/uploads/3/9/4/5/39452505/8846131_orig.png)](https://www.talesoftesting.com/uploads/3/9/4/5/39452505/heeena.png) 

Ever since I have realised the importance of heuristics and oracles, I don’t remember a single day I tested something without using them. Be it for critical thinking, recognising a problem, identifying and analysing risks, test planning or test design; there is heuristic for almost every testing problem. 

I thank all those brilliant people in software testing field who have created heuristics for solving problems. Those heuristics are coming handy for many testers like myself who use them regularly. 

I don’t deny that using multiple heuristics and oracles to solve/recognize some problem helps; but applicability of some ideas from different heuristics is subjective to context of each testing assignment i.e. not all ideas from all heuristics/oracles will help you solve/recognize problems. What has always helped me, is ‘knowing the failure patterns’ of systems that I test. To this end I am saying *failure patterns* not specific defects only. 

These failure patterns are likely to change from project to project, or from module to module within the same project, as project and product elements change with it (read [HTSM](http://www.satisfice.com/tools/htsm.pdf) by James Bach) . However, if you are well aware of failure patterns of products you test; it helps you in multiple ways such as:

1. To find obvious as well as predicted problems quickly i.e. risk for analysis and predictions

2. To find more problems that are likely to be created because of those obvious problems 

3. To plan your testing missions 

4. To strategies your testing based on foreseen/predicted **risks** 

When it comes to learning, my experience with people and products is similar. We can’t know one’s nature just in few interactions, can we? Similarly with fewer tests; we can’t conclude something as a consistent or prevailing failure pattern with that product. 

Be it about people or products, we have to spend enough time to understand them well. If systems/products are bigger and complex (which are most of the times)  finding out failure patterns with them becomes tough. What helps in this case is; one’s skill to recognize. Don’t you know people who are very good at ‘knowing others’ in very less time? 

So what are those things that can help you find prevailing failure patterns in your own system? What is that oracle heuristic to create your project specific heuristic? Over the period of time, I realised that it’s HEEENA that helped me create heuristic for my own project. And I hope it will help you too. 

Here is how I would explain HEEENA! 
​

**H – History**

Try to learn history of your product/project. If you know its history well, you stand fair chance to be able to predict its future. You can know its history by:

- learning about past defects and issues 

- learning about important decisions made in past (scope/de-scope) and reasons behind them 

- learning about enhancements suggested for previous versions 

- learning about non-software issues in past (people issues, cross functional teams not co-operating, different programming teams playing blame games)

 Knowing this information will help you figure out where to focus to find problems and what problems to investigate first. 

**E – Explore **

Practice focused exploratory testing, apply different testing heuristics and see if there is any failure that occurs consistently. Does that appear only in one area? Does it occur somewhere else too? Explore, explore and explore until you come to any conclusion. 

**E- Experiment **

So you noticed some problem? What caused it? What test did you perform? Can modifying that test uncover another problem like that? Is it happening on other machines too? How about testing with different users and user permissions? Something is wrong somewhere…. what is it and where is it? Tried focus/defocus, creep and leap or galumphing? 

**E- Experience **

Make best use of your experience. 

- Domain experience

         –  Can your experience of domain come handy? 

        –  System/Product experience 

        – What does your experience with your product tell you? 

- Experience with comparable products 

           – How about your experience with comparable products in market?

          – What were typical failures with them?

          – Do you see that happening in your product too? 

- Experience with Technology

            – Are there any specific and well known problems with technology used in your   product?

E.g. Any add-ins/pre-requisites that are must for your product to work, HTML5 not supported on all web browsers, flash not supported on iOS etc.

- Experience with people 

           –  Are you stuck in between? Found something but not getting it? Who do you think can help you? Business analyst? Fellow tester? A programmer? 

          – Do you know those common/repeated mistakes that your programmers, fellow testers or BAs do or may be their weak areas? Newly joined programmers or BAs are likely to make mistakes or they can be weak in some areas. Can you figure out which areas are likely to be affected because of those mistakes or weakness?

**N- Note Taking **

Make a habit of taking notes while you test. Note down everything that you observe. Not every behaviour shown by product will be catchy enough to tell you there is a problem. But your notes can help you recognize if there are any hidden patterns and failures. Remember, your notes can be your best guides if you write them well. 

**A- Analysis **

If you recognize a problem, try analysing it in all possible ways. Root Cause Analysis of your findings can give you more information that you can refer in future. Your analysis can become important contribution to ‘history’ files of your project. 

So, that was HEEENA which helped me find out heuristic for my own project. Try it and let me know if it worked for you. 

You can download the mindmap (in xmind format) from [here](https://www.dropbox.com/s/jdyuwiawgt7fpnw/HEEENA.xmind). And if you see any benefits/problems with this approach; I will be happy to learn them.