## GPT-4 Passes the Bar Exam
### MEE Data

#### Summary

#### Data Source
In the paper, we reproduced a limited subset of the MEE and MPT Questions for academic purposes but cannot otherwise 
distribute the full set MEE or MPT Questions directly.  However, the Questions for both the MEE and MPT are generally
available from the websites of various state bars, such as from Maryland linked below: 
 * [July 2022 MEE](https://www.mdcourts.gov/sites/default/files/import/ble/examanswers/2022/202207multistateessayexamination.pdf )


#### Data Formatting
As noted, we reproduced a limited subet of the MEE and MPT Questions for academic use purposes but cannot otherwise 
distribute the MEE or MPT Questions directly.   However, links are available above to access the MEE questions.  

First, we extracted the text of the PDF and prepared it to match the approximate formatting of the exam as presented 
(we removed page numbers and other extraneous text).  

For the MEE, we then followed the Question by Question approach we described in the paper, where we presented the model 
with one subquestion at time (as opposed to all of 3-4 subquestions). 

Our Process Followed the following structure -- 

```
< VIGNETTE >

< PROMPT > 
“You are taking the essay portion of the bar exam.  Answer the above question.  Your answer(s) should be lengthy and 
reference all relevant facts and every applicable legal principles/rules.  Facts and law should be addressed with 
specificity.  If multiple legal issues are present, each one should be thoroughly discussed.”

< SINGLE SUBQUESTION > 
```

#### Evaluation of Model Output 
Representative ‘Good’ Answers for both MEE and MPT as helpful aids to evaluate the quality of the outputs produced by
the respective models.  We used these when assigning scores to the respective models.   As we note in the paper and as
displayed in the PDF link provided below “these Representative Good Answers are provided to illustrate how actual 
examinees responded to the Multistate Performance Tests and the Multistate Essay Examination. The Representative Good 
Answers are not “average” passing answers nor are they necessarily “perfect” answers.” 
 * [July 2022 Representative ‘Good’ Answers](https://mdcourts.gov/sites/default/files/import/ble/examanswers/2022/202207uberepgoodanswers.pdf) 

We suggest reading these side-by-side with the output from the models.  There are two Representative ‘Good’ Answers 
examples per subquestion.