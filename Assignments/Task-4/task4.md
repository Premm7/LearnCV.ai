## 🧾 **Assignment 4 – Feature Extraction and Shape Analysis Toolkit**

**Module:** Module 2 – Image Features, Contours, and Shape Descriptors
**Deadline:** Oct 25, 2025
**Level:** 🟢 Beginner → 🟠 Intermediate → 🔴 Advanced
**Points:** 100 points

---

## 🎯 **Objective**

To design and implement a **Feature & Shape Analysis Application** using **OpenCV** and **Streamlit**, which can:

* Detect, extract, and visualize **image features** (edges, corners, blobs)
* Analyze **shapes and objects** using contours and descriptors
* Compute **geometric and moment-based features**

---

## 📚 **Learning Outcomes**

By completing this assignment, students will:

1. Understand and implement **feature detectors** like Harris, Shi-Tomasi, and ORB.
2. Perform **contour-based shape analysis** and compute object properties.
3. Visualize and interpret **moments, aspect ratios, circularity, and convexity defects**.
4. Build a **GUI** for dynamic visualization of detected features and shapes.

---

## 🖼️ **System Design (Streamlit GUI Overview)**

### **1️⃣ Sidebar – Operations Panel**

Operations grouped by feature type:

**A. Feature Detection**

* Harris Corner Detector
* Shi–Tomasi Corner Detection
* ORB Keypoint Detection
* FAST / SIFT (advanced option)

**B. Shape Analysis**

* Find Contours
* Compute Area & Perimeter
* Approximate Polygon / Bounding Box
* Convex Hull / Convexity Defects
* Fit Ellipse / Circle

**C. Feature Descriptors**

* Hu Moments
* Contour Moments (M00, M10, M01, etc.)
* Aspect Ratio, Extent, Solidity, Circularity

---

### **2️⃣ Main Area – Visualization Panels**

| Left               | Right                                                           |
| ------------------ | --------------------------------------------------------------- |
| **Original Image** | **Processed Output** (features / contours / shapes highlighted) |

Below:
🧾 **Feature Statistics Table** (moment values, counts, etc.)

---

## 🛠️ **Step-by-Step Implementation**

### **Phase 1 – Setup and GUI Skeleton**

* Reuse or adapt Assignment 1 layout.
* Sidebar → Feature and Shape Analysis menu.
* Display uploaded image side-by-side with processed output.

---

### **Phase 2 – Feature Detection**

Implement at least **two methods**:

```python
cv2.cornerHarris()      # Harris detector
cv2.goodFeaturesToTrack() # Shi–Tomasi
cv2.ORB_create()        # ORB keypoints
```

Visualize detected points using colored circles.
Optional: Add sliders for threshold/tuning parameters.

---

### **Phase 3 – Contour Detection and Shape Features**

Use:

```python
contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```

For each contour:

* Draw contour (`cv2.drawContours`)
* Compute **area, perimeter, centroid**
* Extract shape descriptors:

  * **Aspect Ratio = w/h**
  * **Extent = Area / BoundingRectArea**
  * **Solidity = Area / ConvexHullArea**
  * **Equivalent Diameter = √(4 × Area / π)**
  * **Circularity = 4π × Area / Perimeter²**

Display results as a table using `st.dataframe()`.

---

### **Phase 4 – Moments and Descriptors**

* Compute image moments with `cv2.moments(contour)`.
* Calculate Hu moments (`cv2.HuMoments`) and display in scientific notation.

---

### **Phase 5 – Object Labeling and Comparison**

* Detect multiple objects and label each with its shape type (Triangle, Circle, Rectangle).
* Use approximation: `cv2.approxPolyDP()` to estimate the number of vertices.
* Annotate results on the image (`cv2.putText`).

---

### **Phase 6 – Bonus (Advanced)**

* Integrate SIFT or SURF (need non-free modules).
* Add **Shape Matching** (`cv2.matchShapes()`).
* Real-time mode for webcam object tracking.

---

## 📂 **Deliverables**

1. **Codebase** – `app.py` (Streamlit GUI)
2. **Notebook** – `FeatureShapeAnalysis_<roll_no>.ipynb` (detailed step-wise implementation)
3. **Report (PDF)** – Explain methods, include equations, screenshots, and analysis tables.
4. **Demo Video (Optional)** – < 2 minutes showing GUI usage.

---

## 📊 **Evaluation Rubric**

| Criteria                              |  Points | Description                                       |
| ------------------------------------- | :-----: | ------------------------------------------------- |
| GUI Implementation (Streamlit layout) |    25   | Clear layout, dynamic updates, image side-by-side |
| Feature Detection Accuracy            |    25   | Correct implementation of detectors               |
| Shape Analysis & Descriptors          |    25   | Correct geometry, moments, and labeling           |
| Code Structure & Usability            |    15   | Modular code, comments, UI clarity                |
| Documentation & Report                |    10   | Notebook + PDF clarity, visual explanation        |
| **Total**                             | **100** |                                                   |

---

## 📎 **Resources**

* [OpenCV Feature Detection Docs](https://docs.opencv.org/4.x/df/d54/tutorial_py_features_meaning.html)
* [Contour Features in OpenCV](https://docs.opencv.org/4.x/d1/d32/tutorial_py_contour_properties.html)
* [Moments and Shape Matching](https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html)

---

## ✅ **Submission Instructions**

Same as Assignment 1:

1. Fork `learncv.ai` → `/assignments` branch
2. Add your folder `<roll_no>/` under `/assignments/Task-4/`
3. Include `app.py`, notebook, and report
4. Commit message: `"Task 4: Feature and Shape Analysis Submission"`
5. Submit Pull Request (PR) to `/assignments` branch

---