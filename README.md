# RA-MIRI-Galton-Board-UPC

## 📘 Overview
This project simulates a **Galton board** (also known as a quincunx), a classical experiment used to visualize the **Central Limit Theorem (CLT)**.

Balls are dropped through several levels of pegs. At each level, a ball randomly moves left or right with probability 0.5. After all levels, the number of right moves determines the final bin where the ball lands.

When many balls are dropped, the resulting distribution follows a **binomial law**. As the number of levels increases, this binomial distribution becomes nearly identical to a **normal distribution**, demonstrating the CLT in action.

The code also computes the **Mean Squared Error (MSE)** between the empirical (simulated) and theoretical distributions to quantify their similarity.

---

## ⚙️ Requirements
Make sure you have Python installed (≥ 3.8) and the following packages:
```bash
pip install numpy matplotlib scipy
