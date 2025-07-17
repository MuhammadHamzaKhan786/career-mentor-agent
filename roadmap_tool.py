def get_career_roadmap(field: str) -> str:
    roadmaps = {
        "software development": "1. Learn Python, JavaScript, or Java\n2. Understand OOP & Data Structures\n3. Build Web/Mobile Projects\n4. Learn Git & GitHub\n5. Apply for Internships or Freelance Work",
        
        "data science": "1. Learn Python & Statistics Basics\n2. Master Pandas, NumPy, and Matplotlib\n3. Study Data Cleaning & EDA\n4. Learn Machine Learning (scikit-learn, TensorFlow)\n5. Build Projects & Kaggle Portfolio",
        
        "information security": "1. Learn Computer Networking & OS Fundamentals\n2. Study Ethical Hacking & Linux Basics\n3. Master Tools like Wireshark, Metasploit\n4. Get Certified (CEH, CompTIA Security+)\n5. Practice on Hack The Box / TryHackMe",
        
        "nurse practitioner": "1. Earn BSN (Bachelor of Science in Nursing)\n2. Become a Registered Nurse (RN)\n3. Gain 1–2 years clinical experience\n4. Complete a Nurse Practitioner Program (MSN/DNP)\n5. Pass National NP Certification Exam",
        
        "health services management": "1. Earn a Degree in Health Admin or Public Health\n2. Learn Healthcare Regulations & Insurance\n3. Develop Leadership & Communication Skills\n4. Get Internship/Entry-level Experience\n5. Consider MHA/MBA for advancement",
        
        "digital marketing": "1. Learn SEO, SEM, and Content Marketing\n2. Master Tools like Google Analytics, Facebook Ads\n3. Learn Copywriting and Email Marketing\n4. Run Campaigns and Track KPIs\n5. Build Personal Brand or Freelance Portfolio",
        
        "ui/ux design": "1. Learn Figma, Adobe XD or Sketch\n2. Understand UX Research & Design Thinking\n3. Master Typography, Colors, and Layouts\n4. Build Wireframes & Interactive Prototypes\n5. Create a Portfolio with Case Studies",
        
        "video editing": "1. Learn Adobe Premiere Pro or DaVinci Resolve\n2. Study Editing Theory & Storytelling\n3. Learn Motion Graphics (After Effects)\n4. Practice Audio Syncing & Color Correction\n5. Build a YouTube or Client Portfolio"
    }
    return roadmaps.get(field.lower(), "No roadmap found.")
