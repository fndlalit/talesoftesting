---
title: "Introducing Quality Conscious Software Delivery"
date: 2020-09-13 08:27:43 +0530
categories: [Agile, Devops, Software Delivery, Testing]
---

Considering my experience and what I have been observing in the industry, there seems to be an increasing interest in the idea of Whole Team Quality. The idea itself is not new as far as I know but certainly, there seems to be more awareness and eagerness towards its implementation, lately. 

**Why is it needed and how does it help? **

Well, if you are delivering a product as a team, it is natural that everyone who helps build the product is responsible for its quality, or is supposed to be. And for more on this I would urge you to read [ another article](https://www.stickyminds.com/article/whole-team-testing-whole-team-quality) that I wrote for TechWell on this topic. 

**Where is the problem?**

When I tried to figure out how different organisations and teams are going about Whole Team Quality, I realised that asking everyone in the team to test (or asking programmers to test) and automating as much as possible is what they consider Whole Team Quality to be.

I see several problems with that approach:
- The key problem in my opinion is confusing Testing with Quality- Putting most of the efforts to achieve/improve/assess quality focusing only on the **product**- Caring about quality way later in the process.- Reactive strategy i.e. to address quality concerns and risks **after** they are found in a **product **(which is too late and costly to fix usually)- Over emphasise and reliance mostly on automated checks that do not discover hidden risks or find new information. These checks only assert the known information.
Sure I do support the idea of Whole Team Testing to help achieve Whole Team Quality but  how do you go about it makes the big difference.

Over the last four years, I tried different ideas, did experiments in teams for succeeding with Whole Team Quality. I failed but I learned. I continued to try and eventually I would say I succeeded it in. Succeeded in achieving Whole Team Quality in a meaningful way. The way in which risks are found earlier (even before they manifest as a bug in the product) and the Quality is assessed/analysed/addressed/achieved on every level and by every individual in the team.

**The solution that worked for us**

Based on my experiments and learning, I would like to present the **model** and **framework** I have developed and am still experimenting with. It has given me and my team useful results so far and I would encourage you to ***try it ***too.

** The model: QualiTri for three notions of Quality **

Having deep philosophical discussions with [Michael Bolton](https://twitter.com/michaelbolton) when he peer-reviewed my paper on Whole Team Quality, helped me formulate/conceptualise **QualiTri. **And this model further guided me to create the framework** **for its implementation.

Like I said before, focusing on the **Product** notion of the quality alone is not enough. To succeed with Whole Team Quality, it is equally important to understand **Project** and the **People** notion of quality. They are related and they do affect each other. That said, to **deliver** a quality product we got to be equally conscious about the project and the people notion of the quality.

![](https://talesoftesting.com/wp-content/uploads/2020/09/QualiTri-by-Lalit.png)

**The framework: Quality-conscious Software Delivery **

The challenge was how to really go about implementing QualiTri model in a context. And thinking about it helped me formulate my goal to be to achieve the ***d******elivery of quality products by quality-conscious people using quality-empowering processes.  ***

![](https://talesoftesting.com/wp-content/uploads/2020/09/QCSD-in-framework.png)
How to implement the 4E structure of QCSD can vary from context to context but below is how we implemented it in our team which has worked great for us so far. ![](https://talesoftesting.com/wp-content/uploads/2020/09/QCSD-in-action.png)
Going further in detail of the implementation of 4E structure for QCSD framework would require a series of blog posts. It starts with creating awareness, convincing your team for the need of it, considering their inputs, evaluating the project context and creating the workflows/action items ***together with your team***, and then committing for the efforts needed. It’s a process that takes time. Plus it is highly subjective from project teams to project teams and their contexts. And hence I would rather stop here for now.

**How do we know it worked?**

The Lead Time graph for our team before and during an experimentation phase of QCSD in our team (based on the improvements we did in the processes, consciousness with which all people worked with and keeping quality of the product in mind) reflected the positive impact.
![](https://talesoftesting.com/wp-content/uploads/2020/09/Case-study-at-XING.png)
I believe it was the first sprint in a long time, where we as a team finished all the tickets and pulled more, the so-called testing bottle-neck was minimal and the bugs reported that would make into the backlog or warrant some critical rework post-production were negligible.

Sure, this graph did not remain ideal all the time. Teams change, business contexts change too which affects the overall delivery and quality of the product we end up shipping. But if you know how to go about delivering a quality product by quality-conscious people using quality-empowering processes, I am almost certain you will do way more good than bad. And it’s a win in my opinion.

See if you find it worth the shot. If you would like to borrow my help for consulting/implementing this idea for your team or organisation, it would be my pleasure. ***[Just let me know](mailto:editor@teatimewithtesters.com). ***