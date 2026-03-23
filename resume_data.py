# ============================================================
# resume_data.py — Ayush Shukla's Resume (Auto-generated from DOCX)
# Each chunk = one section, used as RAG context for the chatbot
# ============================================================

RESUME_CHUNKS = [
    """
    PERSONAL INFORMATION:
    Name: Ayush
    Location: Dehradun, India
    Phone: +91-8171967891
    Email: ayushshukla351@gmail.com
    LinkedIn: linkedin.com/in/ayushshuklaa
    """,

    """
    EDUCATION:
    Degree: Bachelor of Technology (B.Tech) in Computer Science & Engineering
    University: Graphic Era Hill University, Dehradun
    Duration: June 2021 – June 2025 (Graduated)

    Relevant Subjects Studied:
    - Data Structures & Algorithms
    - Object-Oriented Programming
    - Operating Systems
    - Database Management Systems
    """,

    """
    TECHNICAL SKILLS:
    Programming Languages: C/C++, Python, JavaScript
    Frontend: React.js, HTML, CSS
    Backend: Node.js, Express.js, REST APIs
    AI/ML: TensorFlow, PyTorch, Scikit-learn, NLP, Deep Learning
    Databases: MongoDB, SQL
    Tools: Git
    Core Concepts: DSA, OOP, OS
    """,

    """
    INTERNSHIP EXPERIENCE:
    Company: Behere Elete Technologies Pvt Ltd
    Role: Software Developer Intern
    Duration: 3 Months (Onsite)

    Key Contributions:
    - Built and enhanced full-stack modules using Node.js, Express, and React.
    - Developed reusable frontend components reducing code duplication by 30%.
    - Designed and optimized REST APIs.
    - Applied MongoDB indexing and query optimization improving response time by 25–35%.
    - Implemented JWT-based authentication with Role-Based Access Control (RBAC).
    - Added structured error handling and validation middleware.
    - Worked in an Agile environment, contributed to debugging and performance improvements.
    """,

    """
    PROJECT: Lung Cancer Detection using Deep Learning
    Type: College Academic Project
    Description: A deep learning-based medical imaging system for cancer detection and staging.

    Technical Details:
    - Used 2D U-Net architecture for segmentation.
    - Input: 2D CT scan images.
    - Output: Segmentation masks identifying tumor regions.
    - Classification models used: Custom CNN, VGG16, VGG19, ResNet50V2, MobileNetV2, DenseNet121.
    - DenseNet121 achieved the highest accuracy.
    - Performed cancer stage classification based on tumor detection.

    Pipeline:
    CT Scan → Preprocessing → U-Net Segmentation → Feature Extraction → Classification → Stage Detection

    Outcomes:
    - Accurate tumor localization
    - Cancer stage identification
    """,

    """
    PROJECT: Social Media Sentiment Analysis
    Type: College Academic Project
    Description: NLP-based sentiment classification system for Twitter data.

    Details:
    - Used Naive Bayes and Random Forest algorithms.
    - Processed Twitter data.
    - Classified sentiment into positive, negative, and neutral.
    - Built backend APIs using Node.js.
    - Created frontend dashboard using Next.js.

    Focus Areas:
    - NLP pipeline development
    - Real-time prediction system
    """,

    """
    PROJECT: StockPred
    Type: College Academic Project
    Description: A learning project to implement and explore the backtracking algorithm using stock data as a use case.

    Details:
    - Built to understand and apply backtracking concepts, not for actual trading.
    - Given stock details as input, the algorithm explores all possibilities using backtracking.
    - Identifies and returns the best option to buy based on exhaustive backtracking logic.
    - Backend implemented using Node.js and Python.
    - Built React frontend for visualization of results.

    Purpose:
    - Academic/learning project to implement backtracking in a practical scenario.
    """,

    """
    HACKATHON PROJECTS:

    Graphic-e-Thon 2025:
    - Built an ATS Resume Checker.
    - Checks whether a resume passes Applicant Tracking Systems (ATS).

    Graphic-e-Thon 2024:
    - Built a Smart AI-powered Todo List.
    - Features: Task prioritization and smart suggestions.
    """,

    """
    ACHIEVEMENTS & COMPETITIONS:
    - Finalist at Graphic-e-Thon 2.0 (2025) — Top 50 across India.
    - 2nd Runner-up in Codeft 2025 inter-college coding competition.
    - AIR 71 in IIIT Allahabad Humblefool Cup 2024.
    - Participated in Graphic-e-Thon 2024.
    """,

    """
    RESEARCH PAPER (IEEE):
    Title: Leaf Disease Detection Using KNN
    IEEE Xplore Document ID: 10840461
    Authors: Priyansha Rawat, Ayush Baurai, Ayush, Daksh Rawat, Vihan Singh Bhakuni, Manika Manwal
    University: Graphic Era Hill University, Dehradun, India
    
    Topic: AI/ML-Based Smart Agriculture & Healthcare System

    Overview:
    - Detection of plant diseases at starting stages using Computer Vision and Machine Learning.
    - Explores deep learning techniques and KNN for identification and classification of plant diseases into four categories: Rust, Scab, Multiple Disease, and Healthy.
    - Uses exploratory data analysis (EDA) techniques instead of CNNs for feature extraction.
    
    Technical Details & Preprocessing:
    - Preprocessing techniques used: Canny edge detection, ROI extraction, Histogram Equalization.
    - Methods invoked: SMOTE (Synthetic Minority Over-sampling Technique) and Transfer Learning for processing data more efficiently and making predictions accurate.

    Contributions:
    - Worked on ML pipeline design.
    - Applied models for disease prediction based on leaf images.
    """,
]


def get_full_resume_context():
    """Returns all resume chunks joined as a single context string for the chatbot."""
    return "\n\n".join(chunk.strip() for chunk in RESUME_CHUNKS)
