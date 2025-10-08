# 📚 MMS-PREP: Comprehensive Study Guide Generator

**Automated system for creating beautiful, comprehensive study guides for any topic - Zero training required!**

Created for MMS Finance students at SIMSREE, but adaptable for any subject.

---

## 🎯 What This Does

This framework allows you to generate **comprehensive HTML study guides** like the Finance Mastery Manual by simply providing:

1. **Topic name** (e.g., "Financial Markets", "Marketing Analytics", "Operations Management")
2. **Trusted resources** (e.g., NISM, SEBI, RBI, industry reports)
3. **Student information** (personalization details)
4. **Module structure** (topics you want to cover)

**Output:** A beautiful, professional HTML study guide with:
- 8+ comprehensive modules
- Real-world examples
- Personalized interview answers
- Practice exercises
- Glossary of terms
- Personalized study roadmap
- Print-ready formatting

---

## 📁 Repository Structure

```
MMS-Prep/
├── README.md                          # This file
├── templates/
│   ├── base-template.html             # Reusable HTML template
│   └── config-schema.json             # Configuration structure
├── configs/
│   ├── finance-example.json           # Finance guide config (reference)
│   └── your-topic-config.json         # Your custom config
├── generated/
│   └── [Generated study guides]       # Output directory
├── scripts/
│   ├── generate.py                    # Main generation script
│   └── claude-code-prompt.md          # Prompt template for Claude Code
├── docs/
│   ├── how-to-use.md                  # Detailed usage guide
│   ├── configuration-guide.md         # Config file documentation
│   └── customization-guide.md         # How to customize templates
└── resources/
    └── [Study resources and links]    # Optional resource storage
```

---

## 🚀 Quick Start (3 Simple Steps)

### Step 1: Create Your Topic Configuration

Copy the example config and customize it:

```bash
cp configs/finance-example.json configs/my-topic-config.json
```

Edit `my-topic-config.json` with your details:
- Topic name
- Student information
- Module structure
- Trusted resources

### Step 2: Generate Your Study Guide

**Option A: Using Claude Code (Recommended)**

1. Open Claude Code
2. Copy content from `scripts/claude-code-prompt.md`
3. Replace `{{CONFIG_FILE}}` with your config file path
4. Run the prompt - Claude will generate your complete guide!

**Option B: Using Python Script**

```bash
python scripts/generate.py --config configs/my-topic-config.json
```

### Step 3: Open Your Guide

```bash
# Your guide is ready in the generated/ folder
open generated/My_Topic_Complete_Guide.html
```

---

## 📋 Configuration File Format

Create a JSON file in `configs/` folder:

```json
{
  "topic": "Your Topic Name",
  "student": {
    "name": "Your Name",
    "program": "MMS Finance",
    "college": "SIMSREE",
    "year": "2025-27",
    "background": {
      "strengths": ["Skill 1", "Skill 2"],
      "experience": "Brief description of relevant experience"
    }
  },
  "target": {
    "goal": "Summer Internship in [Field]",
    "roles": ["Role 1", "Role 2"]
  },
  "modules": [
    {
      "number": 1,
      "title": "Module Title",
      "topics": ["Topic 1", "Topic 2", "Topic 3"],
      "objectives": ["Learning objective 1", "Learning objective 2"]
    }
  ],
  "resources": {
    "primary": ["NISM", "SEBI", "RBI"],
    "companies": ["Company 1", "Company 2"],
    "websites": ["screener.in", "moneycontrol.com"]
  },
  "style": {
    "tone": "mentor-like, encouraging",
    "complexity": "beginner-friendly but comprehensive",
    "examples": "Indian market context"
  }
}
```

**See `configs/finance-example.json` for a complete reference!**

---

## 🎨 Features

✅ **Zero Training Required** - Just provide config, get comprehensive guide
✅ **Fully Customizable** - Adjust modules, resources, styling
✅ **Personalized** - Every guide tailored to student's background
✅ **Professional Design** - Beautiful gradient styling, color-coded sections
✅ **Interview-Ready** - Includes personalized Q&A based on student's experience
✅ **Practice-Oriented** - Real-world exercises and case studies
✅ **Comprehensive** - Covers beginner to advanced levels
✅ **Print-Friendly** - Easy to print or save as PDF
✅ **NISM/SEBI Verified** - Uses trusted institutional sources

---

## 📚 Example Topics You Can Create

- **Finance Topics:**
  - Investment Banking
  - Portfolio Management
  - Risk Management
  - Financial Modeling
  - Derivatives & Options

- **Marketing Topics:**
  - Digital Marketing Analytics
  - Brand Management
  - Consumer Behavior

- **Operations Topics:**
  - Supply Chain Management
  - Lean Six Sigma
  - Operations Analytics

- **Data Science Topics:**
  - Machine Learning for Finance
  - Python for Financial Analysis
  - Statistical Analysis

**Anything you're preparing for!**

---

## 🔧 Advanced Customization

### Modify Template Styling

Edit `templates/base-template.html` to change:
- Color schemes
- Font styles
- Section layouts
- Navigation structure

### Add Custom Sections

In your config file, add custom sections:

```json
{
  "custom_sections": [
    {
      "title": "Industry Expert Interviews",
      "content_type": "interview_format"
    }
  ]
}
```

### Include Additional Resources

Place PDFs, images, or links in `resources/` folder and reference them in your config.

---

## 📖 Documentation

- **[How to Use](docs/how-to-use.md)** - Detailed step-by-step guide
- **[Configuration Guide](docs/configuration-guide.md)** - All config options explained
- **[Customization Guide](docs/customization-guide.md)** - Advanced customization

---

## 🤝 Contributing

This is a personal study tool, but feel free to:
- Add your own config templates
- Improve the base template
- Share successful study guides (anonymized)
- Suggest new features

---

## 📜 License

Free for personal educational use.

---

## 🎓 Credits

Created for **Nakul Nandanwar** (SIMSREE MMS Finance 2025-27)

Built with Claude Code and comprehensive finance knowledge from NISM, SEBI, RBI, and company annual reports.

---

## 💡 Tips for Best Results

1. **Be Specific:** Provide detailed module topics in your config
2. **Use Trusted Sources:** Reference official institutions (NISM, SEBI, RBI)
3. **Personalize:** Include your actual background and experience
4. **Iterate:** Generate, review, and regenerate with improvements
5. **Practice:** Complete the practice tasks in your generated guide

---

## 🚀 Next Steps

1. ✅ Review the example config: `configs/finance-example.json`
2. ✅ Create your own config file
3. ✅ Generate your first study guide
4. ✅ Study and ace your interviews!

**Good luck with your preparation! 📚💪**
