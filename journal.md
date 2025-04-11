## **Working with spaCy in Google Colab** <br>
**Problem 1: `numpy.dtype size changed`** 

**Message:**
```
numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject
```

**Cause:**
This warning occurs due to a binary incompatibility between the installed version of `NumPy` and other compiled packages (e.g., `spaCy`, `blis`, `pandas`, etc.). It often happens when:
- `NumPy` was upgraded or downgraded after installing other packages,
- Or cached binary wheels were built against a different NumPy version.

---

**Problem 2: Installing spaCy in Google Colab**
**Note:**
- `fr_core_news_lg` is **larger and slower**, but **more accurate** and supports **word vectors**.
- Works well for deep NLP tasks, potentially including coreference resolution (if supported).

---

**Problem 3: `%pip install` vs `!pip install`**

| Feature                     | `%pip install`      | `!pip install`        |
|----------------------------|---------------------|------------------------|
| Notebook-aware             | ✅ Yes              | ❌ No                 |
| Installs in correct kernel | ✅ Yes              | ⚠️ Maybe not          |
| Reloads package if needed  | ✅ Yes              | ❌ No                 |
| Works in regular terminal  | ❌ No               | ✅ Yes                |

Use `%pip install` in notebooks for safer and cleaner installs.  
Use `!pip install` when you’re doing a quick setup or in simple Colab use.

---

**Conclusion : Using Coreference Resolution Tools (e.g., Coreferee)**

**Note:**
If you plan to use **Coreferee** or other coreference tools with spaCy in French, be aware:
- These may require **non-Python dependencies** (compiled C/C++),
- Setup in Colab is possible, but more involved,
- The `fr_core_news_lg` model is preferred or required.
