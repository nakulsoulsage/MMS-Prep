# 🤖 CLAUDE CODE PROMPT TEMPLATE

**Copy this entire prompt into Claude Code and replace the placeholders with your details!**

---

## YOUR STUDY GUIDE GENERATION PROMPT

```
You are a senior educator and mentor creating a comprehensive study guide for an MMS student.

I need you to create a complete, professional HTML study guide following this exact specification:

CONFIGURATION:
- Config file: {{PATH_TO_YOUR_CONFIG_FILE}}
  (e.g., /mnt/e/AI and Projects/MMS-Prep/configs/my-topic-config.json)

OR provide configuration inline:

STUDENT INFORMATION:
- Name: {{STUDENT_NAME}}
- Program: {{PROGRAM}} (e.g., MMS Finance)
- College: {{COLLEGE}} (e.g., SIMSREE)
- Year: {{YEAR}}
- Background: {{BRIEF_BACKGROUND}}
  (e.g., "AI automation and analytics experience from SoulSage, ROI tracking, process optimization")

TOPIC DETAILS:
- Topic: {{TOPIC_NAME}}
  (e.g., "Financial Markets", "Marketing Analytics", "Operations Management")
- Target Goal: {{GOAL}}
  (e.g., "Summer Internship in Investment Banking")
- Target Roles: {{ROLES}}
  (e.g., "Equity Research Analyst, Financial Analyst")

MODULES TO COVER (8 modules recommended):

Module 1: {{MODULE_1_TITLE}}
Topics: {{TOPICS_LIST}}
Objectives: {{LEARNING_OBJECTIVES}}

Module 2: {{MODULE_2_TITLE}}
Topics: {{TOPICS_LIST}}
Objectives: {{LEARNING_OBJECTIVES}}

[Continue for all 8 modules...]

Module 8: Interview Readiness
- 50+ technical Q&A
- Personalized "Tell Me About Yourself"
- Behavioral questions with STAR method
- How to position background as strength

TRUSTED RESOURCES TO USE:
- {{RESOURCE_1}} (e.g., NISM)
- {{RESOURCE_2}} (e.g., SEBI)
- {{RESOURCE_3}} (e.g., Company Annual Reports)
- {{OTHER_RESOURCES}}

REAL-WORLD EXAMPLES:
Use these companies/organizations for examples:
- {{COMPANY_1}}
- {{COMPANY_2}}
- {{COMPANY_3}}

REQUIREMENTS:

1. OUTPUT FORMAT: Single comprehensive HTML file
   - File path: /mnt/e/AI and Projects/MMS-Prep/generated/{{Topic_Name}}_Complete_Guide.html

2. DESIGN: Use professional styling with:
   - Gradient header (purple/blue theme)
   - Sticky navigation
   - Color-coded sections:
     * Concept boxes (blue)
     * Example boxes (green)
     * Interview boxes (orange)
     * Practice boxes (purple)
   - Responsive tables
   - Formula code blocks
   - Glossary cards
   - Roadmap timeline

3. STRUCTURE FOR EACH MODULE:
   - Module header with learning objectives
   - Multiple detailed sections
   - Real-world examples from {{COUNTRY/REGION}} context
   - "Interview Speak for {{STUDENT_NAME}}" - Personalized answers connecting their background
   - Practice exercises
   - Checkpoint quiz

4. CONTENT REQUIREMENTS:
   - Beginner-friendly but comprehensive
   - Detailed explanations from first principles
   - Real company/organization examples with actual data
   - Each concept includes:
     * Clear definition
     * Why it matters
     * Real example
     * How to answer in interviews
     * Practice task
   - Verified information from trusted sources

5. INTERVIEW PREPARATION:
   - Module 8 must include 50+ Q&A
   - Personalized "Tell Me About Yourself" using student's background
   - Connect student's experience to topic concepts
   - Behavioral questions with STAR method examples

6. ADDITIONAL SECTIONS:
   - Complete Glossary (100+ terms)
   - Personalized 12-week study roadmap
   - Week-by-week milestones
   - Practice assignments

7. TONE & STYLE:
   - Mentor-like, encouraging, personal
   - References student's background throughout
   - Shows how their existing skills are advantages
   - Action-oriented with clear next steps

EXAMPLE OF "INTERVIEW SPEAK" PERSONALIZATION:

If student has "AI automation and analytics" background:

Question: "What is [concept]?"

Answer structure:
"[Definition]. In my previous work at [Company], I [relevant experience] which gave me practical understanding of this concept. [Explain how background connects to finance concept]. [Show analytical thinking]."

VALIDATION CHECKLIST:
✅ All 8 modules complete with detailed content
✅ Real examples from trusted sources (NISM/SEBI/etc.)
✅ Every module has "Interview Speak for {{STUDENT_NAME}}"
✅ Practice tasks included for each module
✅ 50+ interview Q&A in Module 8
✅ Complete glossary with 100+ terms
✅ 12-week personalized roadmap
✅ Professional HTML styling
✅ Print-ready formatting
✅ File size 150KB+ (comprehensive content)

OUTPUT FILE LOCATION:
/mnt/e/AI and Projects/MMS-Prep/generated/{{Topic_Name}}_Complete_Guide.html

After generating, open the file in browser for review.

CREATE THE COMPLETE COMPREHENSIVE STUDY GUIDE NOW!
```

---

## HOW TO USE THIS PROMPT:

### Step 1: Copy the Prompt Above

Copy everything between the ``` markers.

### Step 2: Replace ALL Placeholders

Replace these placeholders with your actual information:

- `{{STUDENT_NAME}}` → Your name
- `{{PROGRAM}}` → Your program (MMS Finance, MBA, etc.)
- `{{COLLEGE}}` → Your college
- `{{TOPIC_NAME}}` → Subject you're studying
- `{{MODULE_X_TITLE}}` → Your module titles
- `{{TOPICS_LIST}}` → Topics you want covered
- `{{RESOURCE_1}}`, `{{RESOURCE_2}}` → Your trusted sources
- `{{COMPANY_1}}`, `{{COMPANY_2}}` → Companies for examples

### Step 3: Paste into Claude Code

1. Open Claude Code in your terminal
2. Paste the customized prompt
3. Press Enter

### Step 4: Wait for Generation

Claude will:
1. Create comprehensive content for all modules
2. Generate HTML file with professional styling
3. Include personalized interview answers
4. Add glossary and roadmap
5. Save to `generated/` folder
6. Open in your browser

### Step 5: Review & Study!

Your complete study guide is ready!

---

## EXAMPLE FILLED PROMPT:

Here's an example for "Marketing Analytics":

```
STUDENT INFORMATION:
- Name: Rahul Sharma
- Program: MMS Marketing
- College: SIMSREE
- Year: 2025-27
- Background: "3 years in digital marketing at Flipkart, experience with Google Analytics, campaign optimization, data-driven decision making"

TOPIC DETAILS:
- Topic: Marketing Analytics & Data-Driven Marketing
- Target Goal: Summer Internship in Marketing Analytics
- Target Roles: Marketing Analyst, Digital Marketing Analyst, Growth Analyst

MODULES TO COVER:

Module 1: Introduction to Marketing Analytics
Topics: What is marketing analytics, Role of data in marketing, Marketing metrics overview, Digital vs traditional analytics
Objectives: Understand marketing analytics fundamentals, Know key metrics, Differentiate data sources

Module 2: Customer Analytics
Topics: Customer segmentation, RFM analysis, Customer lifetime value, Churn prediction
Objectives: Segment customers effectively, Calculate CLV, Predict churn

[... continue for 8 modules]

TRUSTED RESOURCES TO USE:
- Google Analytics Academy
- HubSpot Marketing Statistics
- Nielsen Reports
- Company case studies (Flipkart, Amazon India, Swiggy)

REAL-WORLD EXAMPLES:
- Flipkart
- Amazon India
- Zomato
- Swiggy
- Myntra
```

---

## 💡 TIPS FOR BEST RESULTS:

1. **Be Specific:** List exact topics you want covered
2. **Provide Context:** Include your actual background/experience
3. **Use Real Resources:** Name specific institutions/reports
4. **List Companies:** Choose relevant companies for your field
5. **Define Objectives:** Clear learning goals for each module

---

## ⚡ QUICK CUSTOMIZATION OPTIONS:

Want to modify the generated guide?

**Change Color Scheme:**
Add to prompt: "Use [color] gradient theme instead of purple/blue"

**Different Structure:**
Add to prompt: "Organize as 10 modules instead of 8" or "Include case study section"

**More Examples:**
Add to prompt: "Include 3 detailed case studies per module"

**Different Focus:**
Add to prompt: "Focus more on practical application" or "Include more theoretical frameworks"

---

## 🆘 TROUBLESHOOTING:

**Guide not comprehensive enough?**
- Add: "Make each module at least 5000 words with detailed examples"

**Need more interview questions?**
- Add: "Include 100 interview questions in Module 8"

**Want different styling?**
- Add: "Use minimalist design" or "Include more visual elements"

**Need specific frameworks?**
- Add: "Include [Framework Name] analysis in Module X"

---

## 📚 SAVED PROMPTS:

Save your customized prompts in this folder for reuse!

Create a file: `configs/my-topic-prompt.txt`

Next time, just copy and paste!

---

**Ready to generate your study guide? Copy the prompt above and customize it! 🚀**
