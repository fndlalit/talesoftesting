---
title: "Quality Experience(QX): Co-creating Quality Experience for everyone associated with the product."
date: 2020-07-03 17:00:00 +0530
categories: [Devops, Software Delivery, UX]
image: "https://images.unsplash.com/photo-1553877522-43269d4ea984?w=800&h=400&fit=crop"
---

![](/assets/img/posts/1593763088951.png)
 
I have been talking about [**Whole Team Qualit**](https://contestnyc2019.sched.com/event/Tk13/2-day-certification-training-succeeding-with-whole-team-testing)**y** via [Whole Team Testing](https://www.stickyminds.com/article/whole-team-testing-whole-team-quality) for a couple of years now. During my workshops, I am often asked if testing can only be extended for programmers in a team. Pretty interesting question it is and my answer is obviously “no”. Though I usually explain in my workshops on how to extend testing to roles beyond programmers in a team i.e. for UX or PO roles, I realized that I have not given deep thought to it and to how exactly testing could be extended to other disciplines in a meaningful way.

I read books, discussed with my colleagues, did my research and the outcome has been what I would like to name as QX i.e. Quality Experience. If QA (read that as Quality Advocates) and UX professionals collaborate in a meaningful way, I firmly believe they can co-create a Quality Experience for everyone associated with the product.

**So, what is QX after all?
**
QX stands for Quality Experience. For sake of understanding, you can call it a marriage between QA (read it as Quality Advocacy please) and UX. After some need-based discussions and interactions with my UX colleagues, I realized that we can achieve a lot more if we work closely together regularly. The key idea of QX is about facilitating the collaboration between QA and UX so that they can contribute to what I would call a “Quality Experience” of the product. This is both for the end-user and for those who build the product itself.

I believe that with some process optimizations, mindset enablers for testers as well as UX designers, and following some heuristics I have created, it is possible to kickstart the QX journey if that idea interests you.
**But what’s the need? Is QA alone not enough to cater to product quality (or UX alone not enough for better user experience)? **

Well, I am afraid, it is not. Not at-least when you believe that *Quality is value to someone (who matters) *and when multiple stakeholders matter at the same time.
Let me explain. Imagine that a new design change required in a product is a revenue booster for the company but it is also likely to impact the user experience. Testers often end up with oracle problem in such situations and can not decide what their quality criteria should look like. Of course, the Product Owner can be consulted here for a final decision but that’s not the point. We testers are in the information business, after all (yes, even if you follow the Modern Testing). I find it important for testers to be able to make a comprehensive information gathering and present that information to decision-makers so that they can make an informed decision based on that.

Now, if testers lack the tools and mindset to figure out how to go about solving such problems and gathering information that would matter, their job would be poorly done. And if you are still not convinced, I highly recommend you to read Weinberg’s latest book around [System Design Heuristics](https://leanpub.com/systemdesignheuristics). This book could not have come at any other better time for me. I started reading it while working on the QX concept and it has given me some interesting insights to sharpen my thinking around this topic.

On the other hand, let’s assume that a UX/Interaction designer has been given a problem to solve or has been asked to create a new solution for some product. How do they ensure they have gathered enough information to do that job right? How about historical incidents or say hidden technical challenges or simply put edge case scenarios, cross-functional dependencies, and so on? I believe that having this information at hand can greatly benefit how UX designers can approach the problem and solve that in a better way.

Therefore I think that an engagement between UX and QA can help both of them to perform their job even better. And hence QX seems to be a good way to go about it.

**Well, how does it work?**

Here are some ideas that I experienced to be working quite well. See if they work for you too?

**1. Cross-discipline training for QA and UX **

For successful collaboration, it is important that QA and UX understand each other well and that they speak and understand each other’s language. More important is to understand the mindset with which they both operate.

I have experienced difficulties in understanding UX’s point of view sometimes and my UX colleagues made the same experience. But a conscious effort made towards understanding each others’ language helped us solve those issues and facilitating the collaboration thereby.

That said, we recommend that testers and UX designers start from understanding each other’s roles and mindset. Attending cross-discipline training should help but if that is not possible, try doing “pairing sessions” at least.

**2. Process changes or optimizations  **

A great deal of it depends on what kind of team set up you have. Some teams may have dedicated UX designers, some organizations have UX teams as a “lateral” service provider for different teams and some teams simply don’t have UX people. Their designs are usually outsourced or made by engineers themselves.  Some recommendations I would like to make here are:
1. Involve testers as early as possible and make them also part of the design process/discussions. UX will thank them for lots of useful info which might result in the faulty design if missed.

2. Early and frequent communication between UX and QA would help. Try “brainstorming” sessions for early design stages. Ask tester for hidden scenarios or technical hacks to go around things. Ask them for user complaints or known production issues surrounding the design under discussion.

3. Testers may perform focused UX testing and consult UX from time to time for their design-related findings. A “pair testing” session with UX expert can greatly benefit testers for more test ideas surrounding usability and human-computer interaction under different contexts.

4. Instead of creating a misinformed bug report surrounding usability and UX, testers can always consult UX colleagues first for feedback around their findings and use them as their oracles. Most of the time, UX people have information and insights (from their interaction with real users, test sessions they perform, qualitative and quantitive data analysis they do, etc.) that explain why that design is made a certain way.
5. Not every design change goes via the standard UX lead design process. Engineers sometimes have to make decisions that may result in a change in product design or impact certain product behaviors. Such changes can always be sent to UX designers for their feedback. The tester can play a big role in making this activity happen on behalf of the engineering team.

**3. UX testing heuristics for testers **

Mere exchange with UX colleagues without having proper knowledge of how to test for better user experience can be futile. Which is why I recommend testers to get good at UX testing too. By that, I don’t mean typical usability testing or accessibility testing alone. After giving a deep thought to all possibilities involved, I have come up with the following heuristic for testers.

Keep in mind that it can also be used as a means to facilitate collaboration and have a better discussion with UX colleagues. Not everything might be applicable for all the contexts. Choose those that fit best in your context. Here you go:

**Problem** -To come up with relevant test ideas, Testers and UX must be on the same page in terms of understanding the problem they want to solve with the proposed design. UX often get first-hand information from the PO about the problems, which testers sometimes are lacking. Trying to understand what problem UX wants to solve with their solution, can open up lots of possibilities for testers and confine them to think in the right direction. It would also spare them from coming up with the right questions and perform better impact analysis of the change.
- What product problem are you testing the UX solution against?- Is the problem simple to understand or has complexities within itself? Can you break it down further? Ask for more information if that helps to understand the problem better.- Rule of Three (thank you Jerry Weinberg) – If you can’t think of at least three ways the design could fail, you haven’t tested the design enough. What to do about those identified potential failures is another thing. But it would be worth to identify them and at-least discuss those possibilities with UX or PO. (Pro tip – Don’t overdo it)
**User Needs – **
This is highly subjective and might vary from project to project. The key idea is to understand what User Needs are getting addressed through the design and if you as a tester can foresee any challenges/impact of that. This can also be very well made as a part of ‘understanding the problem’ part. It does not matter how you do it, but what matters most is that you know what aspects of user needs you are dealing with.
- What user needs have been used to design the solution?- Do you understand those user-needs in the context of a given problem and your product feature?- Based on your product knowledge, do you find the user-needs ‘selected’ suitable for the designed solution?- Is there anything (information around business/technical/cross-team constrains/special scenarios etc.) that invalidates or challenges the user-needs that are taken into account?
**User vs Business Needs **
- What is the goal of the solution provided? Is it for ease of business for products or for improving user experience?- Is the change in your product feature adversely impacting other parts of the application (other teams) in terms of User Experience or KPI? – Inform the stakeholders- Can you borrow supporting data/statistics from UX/PO to understand their rationale better? – e.g. Why this screen size and why not this? Because we have only so and so number of users using that. And thus the impact is minimal.- Does an attempt of “ease of business” compromise “user experience”?- Does improving the “user experience” goal impact business/product KPIs?
**Finding Balance – Solving the Oracle Problem **

When you as a tester are unable to decide if the proposed solution is good for the product but bad for users and vice versa, use some of the methods below to make your decision-making more concrete and practical. Based on the configurations of teams, there may be no dedicated UX expert to cater to these needs. It is therefore advisable for testers that they wear UX hats and find the balance by asking the right questions before it is too late.

Plenty of efforts could be saved if testers too are involved in design/UX decisions early where dedicated UX expert is absent or designs have been made by third party services etc.

**What Must Not Change?**

Whatever we ultimately do, what are the things you don’t want to be changed? (from [System Design Heuristics](https://www.goodreads.com/book/show/40013864-system-design-heuristics) by Jerry Weinberg)

Introducing design changes in an existing product that are targeted at a specific goal by UX designers, can harm things that are not meant to be affected by that. I highly doubt if there are deliberate efforts made to analyze this regression impact on the design level itself. This is why, if a tester asks this question right in the early phase of a design change, it is likely to save lots of rework for the later.

“If we don’t start that way, it’s all too easy to lose track of the unchangeable.” – Jerry Weinberg.

**Impact Analysis
**
What are the visible and invisible parts of the product that are impacted by this change? And what is the impact?
- GUI process flow : For the end-user and for internal users- Impact on user’s feelings – Happy? Overwhelming? Confusing? Irritating? Unexplainable?- Impact on cross-functional teams ( talk to them early and discuss for a possible solution)- When the design is independent of user-needs/user dataBasic Rules- Usability Ergonomics- Heuristic from Jacob Nielsen- FCC CUTS VIDS- UX Checklist (chrome extension)
**Creativity**

Running out of test ideas to decide if the solution is perfect? Pour some creativity in.
- Consistency with Comparable products/competition – Is this solution consistent or competent with comparable products/solutions in the market?- Inspiration from various fields of study and domains **for ideas** (not correctness) –Philosophy- Social Science- Gender, Age and Geographical studies- Medical domain- E-commerce Domain- Fashion Domain- Others?
**Exactness, Intuitive and Counter-intuitive Design**

Most of the time, testers are more focused on the technical and functional aspects of the product so much that they unknowingly tend to ignore looking for obvious problems. A deliberate attempt needs to be made to look at the product like an unexperienced user to see if they will understand what we expect them to. To do this:
- Check text/labels of your menu items, action buttons, information tables, and even terms and conditions – Are they obvious and intuitive? Are they confusing users? Is there more than one possible meaning?- Is the ‘interaction’ between components intuitive and obvious? What are the abnormalities? How are they different from common use conventions?- Are the terms you are using to explain things/menus/actions confusing? Can they be understood by the typical user easily? Are there any cultural constraints that might backfire? How do we avoid misunderstandings?
Well, I wish I could work on this and develop this idea even further. But for the benefit of time, I would stop here. Maybe I would get back to this again when I have more ideas. But in the meantime, feel free to comment below and share more ideas if you like. And do not forget to tell me how you find the QX idea so far.

And, I recommend you to read  [System Design Heuristics](https://www.goodreads.com/book/show/40013864-system-design-heuristics) by Jerry Weinberg. The book gave me lots of ideas to ponder upon.

Until then…

[![](/assets/img/posts/QX-for-Testers.png)](/assets/img/posts/QX-for-Testers.png)