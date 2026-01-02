# 📖 HOW TO USE: MMS-PREP Study Guide Generator

**Complete step-by-step guide for creating comprehensive study materials**

---

## 🎯 Overview

This system allows you to generate professional, comprehensive study guides on ANY topic without any AI training. You just provide:
1. Topic details
2. Module structure
3. Trusted resources

And get a complete HTML study guide with examples, practice tasks, interview prep, and more!

---

## 🚀 QUICK START (5 Minutes)

### Step 1: Choose Your Topic

Decide what you want to study:
- Financial Markets
- Marketing Analytics
- Operations Management
- Data Science for Business
- Supply Chain Analytics
- Any other MMS/MBA subject

### Step 2: Create Configuration File

```bash
cd /mnt/e/AI\ and\ Projects/MMS-Prep/configs
cp finance-example.json my-topic.json
```

Edit `my-topic.json` with your details.

### Step 3: Use the Claude Code Prompt

1. Open: `scripts/claude-code-prompt.md`
2. Copy the prompt template
3. Replace placeholders with your config details
4. Paste into Claude Code
5. Wait for generation (~2-5 minutes)

### Step 4: Access Your Guide

```bash
cd /mnt/e/AI\ and\ Projects/MMS-Prep/generated
# Your guide will be here: YourTopic_Complete_Guide.html
```

Open in browser and start studying!

---

## 📋 DETAILED WALKTHROUGH

### Phase 1: Planning Your Study Guide

**1.1 Define Your Learning Goals**

Ask yourself:
- What role am I preparing for?
- What interviews do I need to ace?
- What's my timeline? (recommended: 8-12 weeks)
- What's my current knowledge level?

**Example:**
```
Role: Equity Research Analyst
Timeline: 12 weeks
Current Level: Finance beginner
Goal: Ace summer internship interviews
```

**1.2 Identify Trusted Resources**

List official sources for your topic:
- Regulatory bodies (SEBI, RBI, etc.)
- Industry associations (NISM, CFA Institute, etc.)
- Leading companies in the field
- Academic institutions
- Professional certifications

**Example for Finance:**
- NISM, SEBI, RBI
- HDFC Bank, Infosys, TCS annual reports
- CFA Institute resources

**1.3 Structure Your Modules**

Break your topic into 8 logical modules:
- Modules 1-3: Foundations
- Modules 4-6: Core concepts
- Module 7: Advanced/Applied
- Module 8: Interview readiness

**Example for Finance:**
1. Understanding Finance
2. Financial Statements
3. Financial Ratios
4. Valuation & DCF
5. Equity Markets
6. Equity Research
7. Corporate Finance
8. Interview Prep

---

### Phase 2: Creating Configuration

**2.1 Student Information Section**

```json
{
  "student": {
    "name": "Your Name",
    "program": "MMS/MBA Marketing",
    "college": "Your College",
    "year": "2025-27",
    "background": {
      "strengths": [
        "Skill 1 you have",
        "Skill 2 you have",
        "Skill 3 you have"
      ],
      "experience": "Brief description of relevant work experience"
    }
  }
}
```

**Why this matters:**
- Creates personalized interview answers
- Connects your experience to new concepts
- Positions your background as advantage

**2.2 Module Structure Section**

For each of your 8 modules:

```json
{
  "number": 1,
  "title": "Clear descriptive title",
  "topics": [
    "Specific topic 1",
    "Specific topic 2",
    "Specific topic 3"
  ],
  "objectives": [
    "What you'll learn 1",
    "What you'll learn 2"
  ],
  "depth": "beginner/intermediate/advanced"
}
```

**Tips:**
- Be specific with topics (not "Marketing" but "Customer Segmentation Using RFM Analysis")
- List 4-6 topics per module
- Set realistic depth level

**2.3 Resources Section**

```json
{
  "resources": {
    "primary_institutions": ["Institution 1", "Institution 2"],
    "companies_for_examples": ["Company 1", "Company 2", "Company 3"],
    "data_sources": ["Where to get data"],
    "learning_resources": ["Additional resources"]
  }
}
```

**Example for Marketing:**
```json
{
  "primary_institutions": ["Google Analytics Academy", "HubSpot Academy"],
  "companies_for_examples": ["Amazon India", "Flipkart", "Swiggy"],
  "data_sources": ["SimilarWeb", "App Annie", "Company investor decks"],
  "learning_resources": ["Google Digital Garage", "Meta Blueprint"]
}
```

---

### Phase 3: Generation

**3.1 Using Claude Code Prompt (Recommended)**

1. Open `scripts/claude-code-prompt.md`
2. Copy the entire prompt
3. Customize all `{{PLACEHOLDERS}}`:
   - `{{STUDENT_NAME}}` → Your actual name
   - `{{TOPIC_NAME}}` → Your topic
   - `{{MODULE_1_TITLE}}` → Your module titles
   - etc.
4. Open Claude Code in your terminal
5. Paste the customized prompt
6. Press Enter

**What happens:**
- Claude reads your config
- Generates comprehensive content for all 8 modules
- Creates HTML with professional styling
- Includes personalized interview answers
- Adds glossary with 100+ terms
- Creates 12-week roadmap
- Saves to `generated/` folder
- Opens in browser

**Time:** 2-5 minutes depending on complexity

**3.2 Alternative: Manual Prompting**

If you prefer more control:

```
Create a comprehensive HTML study guide for [TOPIC].

Student: [NAME], [PROGRAM], [COLLEGE]
Background: [YOUR EXPERIENCE]
Goal: [YOUR GOAL]

Modules to cover:
1. [MODULE 1]
2. [MODULE 2]
...

Use resources: [RESOURCES]
Include examples from: [COMPANIES]

Requirements:
- Beginner-friendly but comprehensive
- Include "Interview Speak for [NAME]" sections
- Add practice tasks
- Create glossary
- Add 12-week roadmap

Save to: /mnt/e/AI and Projects/MMS-Prep/generated/[Topic]_Guide.html
```

---

### Phase 4: Using Your Study Guide

**4.1 First Review**

When your guide is generated:
1. Open in browser
2. Skim the table of contents
3. Check Module 8 (Interview Prep) - these are your end goals
4. Review the 12-week roadmap
5. Bookmark key sections

**4.2 Study Schedule**

Follow the roadmap:
- **Week 1:** Module 1 + start building knowledge base
- **Week 2:** Module 2 + practice with real data
- **Weeks 3-4:** Modules 3-4 + deep dive into concepts
- **Weeks 5-8:** Modules 5-7 + applications
- **Weeks 9-12:** Module 8 + interview practice

**4.3 Active Learning**

For each module:
1. **Read:** Go through concepts thoroughly
2. **Practice:** Complete the practice tasks (important!)
3. **Apply:** Use real company data
4. **Test:** Complete checkpoint quizzes
5. **Review:** Study "Interview Speak" sections

**4.4 Practice Tasks**

Most modules include practice tasks like:
```
Using Screener.in (or similar platform):
1. Find [Company] financials
2. Calculate [specific ratios]
3. Compare with competitors
4. Write brief analysis
```

**DO THESE!** They're crucial for interview preparation.

**4.5 Interview Preparation**

Module 8 approach:
1. **Week 9:** Read all 50+ Q&A, understand the logic
2. **Week 10:** Customize answers with your experience
3. **Week 11:** Practice out loud, record yourself
4. **Week 12:** Mock interviews with friends/mentors

---

## 🎨 CUSTOMIZATION OPTIONS

### Changing Design

Want different colors? In your prompt, add:

```
Use [COLOR] gradient theme instead of purple/blue
Example: "Use green/teal gradient" or "Use minimalist black/white"
```

### Adding Sections

Want case studies? Add to config:

```json
{
  "custom_sections": [
    {
      "title": "Industry Case Studies",
      "count": 3,
      "companies": ["Company 1", "Company 2", "Company 3"]
    }
  ]
}
```

### More Examples

Want more examples per module?

In prompt: "Include at least 5 real company examples per module"

### Different Structure

Want 10 modules instead of 8?

Just define 10 modules in your config!

Want different focus?

Add: "Focus 60% on practical application, 40% on theory"

---

## 📊 QUALITY CHECKLIST

After generation, verify:

✅ **Completeness**
- [ ] All 8 modules present and detailed
- [ ] Each module has 4+ sections
- [ ] Examples from trusted sources
- [ ] Practice tasks included

✅ **Personalization**
- [ ] Student name appears throughout
- [ ] "Interview Speak for [You]" sections present
- [ ] Background connected to concepts
- [ ] Behavioral answers use your experience

✅ **Interview Readiness**
- [ ] 50+ technical Q&A in Module 8
- [ ] "Tell Me About Yourself" personalized
- [ ] Behavioral questions with STAR method
- [ ] Quick revision summaries

✅ **Additional Content**
- [ ] Glossary with 100+ terms
- [ ] 12-week roadmap with milestones
- [ ] Practice assignments
- [ ] Resource links

✅ **Formatting**
- [ ] Professional styling
- [ ] Color-coded sections
- [ ] Readable fonts
- [ ] Tables formatted correctly
- [ ] Print-friendly

**File Size Check:**
- Minimum: 150KB (comprehensive content)
- Ideal: 180-250KB (very comprehensive)
- If less than 100KB: Not enough detail, regenerate

---

## 🔧 TROUBLESHOOTING

### Problem: Generated guide is too basic

**Solution:**
Add to prompt: "Make each module at least 5000 words. Include detailed explanations from first principles. Add multiple examples per concept."

### Problem: Not enough interview questions

**Solution:**
Add to prompt: "Module 8 must include exactly 100 interview questions with detailed answers."

### Problem: Examples not relevant to India

**Solution:**
Specify: "All examples must use Indian companies and Indian market context. Use data from [specific Indian companies]."

### Problem: Missing personalization

**Solution:**
Emphasize: "Every 'Interview Speak' answer must connect to [Student Name]'s background in [specific experience]. Reference their work at [Company] in explanations."

### Problem: Too technical/Not beginner-friendly

**Solution:**
Add: "Explain every concept from absolute basics. Assume zero prior knowledge. Use simple analogies before technical definitions."

### Problem: Generation incomplete

**Solution:**
Claude might hit token limits. Try:
- Reduce to 6 modules instead of 8
- OR split into 2 prompts (Modules 1-4, then 5-8)
- OR reduce examples per module

---

## 💡 ADVANCED USAGE

### Creating Multiple Guides

For comprehensive preparation:

1. **Core Subject Guide** (Finance/Marketing/Operations)
2. **Interview Skills Guide** (Behavioral + Technical)
3. **Company Research Guide** (Target companies)
4. **Case Study Guide** (Practice cases)

### Updating Existing Guide

Want to add content to your guide?

1. Open the generated HTML
2. Use Claude Code to add sections:
   ```
   Read: /path/to/existing_guide.html
   Add a new section on [TOPIC] after Module [X]
   Include examples and practice tasks
   Save updated file
   ```

### Collaborative Study

Share your config files with classmates:
- They can generate with their own names
- Creates personalized versions for each person
- Study together with same structure

---

## 📚 EXAMPLE WORKFLOWS

### Example 1: Finance Student

```
Week 1: Create Finance guide
Week 2-3: Study Modules 1-3
Week 4: Create "Valuation Deep Dive" guide
Week 5-6: Study both guides
Week 7: Create "Interview Mastery" guide (behavioral focus)
Week 8-12: Practice all three
```

### Example 2: Marketing Student

```
Week 1: Create Marketing Analytics guide
Week 2: Create Digital Marketing guide
Week 3-8: Study both alternating weeks
Week 9: Create Case Studies guide
Week 10-12: Practice cases + interviews
```

---

## 🎓 BEST PRACTICES

1. **Start Early:** Don't wait till last month
2. **Be Specific:** Detailed configs = better guides
3. **Do Practice Tasks:** Theory alone isn't enough
4. **Customize Answers:** Don't memorize, understand
5. **Update Regularly:** Add notes as you learn
6. **Share Learnings:** Study groups help
7. **Track Progress:** Check off objectives
8. **Mock Interviews:** Practice makes perfect

---

## 🆘 GETTING HELP

**If you're stuck:**

1. Check `configs/finance-example.json` for reference
2. Review the generated Finance guide
3. Read `claude-code-prompt.md` carefully
4. Try the simple example first
5. Iterate - first version doesn't have to be perfect!

---

## ✅ NEXT STEPS

Now that you understand how to use the system:

1. [ ] Decide on your first topic
2. [ ] Create your config file
3. [ ] Customize the Claude Code prompt
4. [ ] Generate your first guide
5. [ ] Start studying!
6. [ ] Iterate and improve

**You've got this! 🚀**

---

**Questions or improvements? Document them in your own notes and iterate!**
