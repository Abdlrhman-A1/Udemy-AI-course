# استيراد مكتبة Matplotlib
import matplotlib.pyplot as plt  # مكتبة لتصميم الرسوم البيانية

# الدالة الأولى: رسم خطي Line Plot
def line_plot(x, y, title, xlabel, ylabel):
    plt.figure()  # إنشاء شكل جديد للرسم
    plt.plot(x, y, marker='o', linestyle='-', color='b')  # رسم خط مع تحديد العلامات
    plt.title(title)  # إضافة عنوان للرسم
    plt.xlabel(xlabel)  # تسمية محور X
    plt.ylabel(ylabel)  # تسمية محور Y
    plt.grid(True)  # تفعيل الشبكة
    plt.show()  # عرض الرسم البياني

# الدالة الثانية: رسم بياني عمودي Bar Chart
def bar_chart(categories, values, title, xlabel, ylabel):
    plt.figure()  # إنشاء شكل جديد للرسم
    plt.bar(categories, values, color='orange')  # رسم الأعمدة
    plt.title(title)  # إضافة عنوان
    plt.xlabel(xlabel)  # تسمية المحور الأفقي
    plt.ylabel(ylabel)  # تسمية المحور الرأسي
    plt.show()  # عرض الرسم

# الدالة الثالثة: رسم دائري Pie Chart
def pie_chart(labels, sizes, title):
    plt.figure()  # إنشاء شكل جديد
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)  # رسم الدائرة
    plt.title(title)  # إضافة عنوان
    plt.show()  # عرض الرسم

# الدالة الرابعة: رسم مبعثر Scatter Plot
def scatter_plot(x, y, title, xlabel, ylabel):
    plt.figure()  # إنشاء شكل جديد
    plt.scatter(x, y, color='green')  # رسم النقاط
    plt.title(title)  # إضافة عنوان
    plt.xlabel(xlabel)  # تسمية المحور الأفقي
    plt.ylabel(ylabel)  # تسمية المحور الرأسي
    plt.grid(True)  # تفعيل الشبكة
    plt.show()  # عرض الرسم

# الدالة الخامسة: خريطة حرارية Heatmap
def heatmap(data, title):
    plt.figure()  # إنشاء شكل جديد
    plt.imshow(data, cmap='hot', interpolation='nearest')  # رسم الخريطة
    plt.title(title)  # إضافة عنوان
    plt.colorbar()  # إضافة شريط الألوان
    plt.show()  # عرض الرسم

# الدالة السادسة: رسم ثلاثي الأبعاد 3D Plot
from mpl_toolkits.mplot3d import Axes3D  # لاستيراد أدوات الرسم ثلاثي الأبعاد
def plot_3d(x, y, z, title):
    fig = plt.figure()  # إنشاء شكل جديد
    ax = fig.add_subplot(111, projection='3d')  # إضافة محور ثلاثي الأبعاد
    ax.plot(x, y, z, color='red')  # رسم الخط
    ax.set_title(title)  # إضافة عنوان
    plt.show()  # عرض الرسم

# أمثلة لاستخدام كل دالة:

# 1. رسم خطي
line_plot(
    x=[1, 2, 3, 4], 
    y=[10, 20, 15, 25], 
    title="Line Plot Example", 
    xlabel="Time", 
    ylabel="Value"
)

# 2. رسم بياني عمودي
bar_chart(
    categories=["A", "B", "C"], 
    values=[50, 30, 70], 
    title="Bar Chart Example", 
    xlabel="Category", 
    ylabel="Frequency"
)

# 3. رسم دائري
pie_chart(
    labels=["Apple", "Banana", "Cherry"], 
    sizes=[40, 30, 30], 
    title="Pie Chart Example"
)

# 4. رسم مبعثر
scatter_plot(
    x=[1, 2, 3, 4], 
    y=[5, 15, 10, 20], 
    title="Scatter Plot Example", 
    xlabel="X-axis", 
    ylabel="Y-axis"
)

# 5. خريطة حرارية
heatmap(
    data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
    title="Heatmap Example"
)

# 6. رسم ثلاثي الأبعاد
plot_3d(
    x=[1, 2, 3], 
    y=[4, 5, 6], 
    z=[7, 8, 9], 
    title="3D Plot Example"
)

# المكتبات المطلوبة للتثبيت:
# pip install matplotlib
# ##################################################

# استيراد مكتبة Matplotlib
import matplotlib.pyplot as plt
import numpy as np  # لاستعمال الأرقام والمصفوفات بسهولة

# الدالة الأولى: رسم عدة رسوم في نفس الشكل (Subplots)
def multiple_subplots():
    x = np.linspace(0, 10, 100)  # إنشاء قيم x متدرجة بين 0 و 10
    plt.figure(figsize=(10, 6))  # إنشاء شكل بحجم مخصص

    # الرسم الأول
    plt.subplot(2, 2, 1)  # تقسيم الشكل لـ 2x2 ورسم الشكل الأول
    plt.plot(x, np.sin(x), color='blue')
    plt.title("Sine Wave")  # عنوان الرسم الأول

    # الرسم الثاني
    plt.subplot(2, 2, 2)  # الرسم في الجزء الثاني
    plt.plot(x, np.cos(x), color='green')
    plt.title("Cosine Wave")  # عنوان الرسم الثاني

    # الرسم الثالث
    plt.subplot(2, 2, 3)  # الرسم في الجزء الثالث
    plt.plot(x, np.exp(-x), color='red')
    plt.title("Exponential Decay")  # عنوان الرسم الثالث

    # الرسم الرابع
    plt.subplot(2, 2, 4)  # الرسم في الجزء الرابع
    plt.plot(x, x**2, color='purple')
    plt.title("Quadratic Growth")  # عنوان الرسم الرابع

    plt.tight_layout()  # تحسين توزيع الأشكال
    plt.show()  # عرض الشكل

# الدالة الثانية: رسم هيستوجرام (Histogram)
def histogram_example(data):
    plt.figure(figsize=(8, 6))  # إنشاء شكل جديد بحجم محدد
    plt.hist(data, bins=10, color='orange', edgecolor='black')  # رسم هيستوجرام مع 10 أعمدة
    plt.title("Histogram Example")  # عنوان الرسم
    plt.xlabel("Values")  # تسمية المحور الأفقي
    plt.ylabel("Frequency")  # تسمية المحور الرأسي
    plt.show()  # عرض الرسم

# الدالة الثالثة: رسم بيانات بخطوط متنوعة (Styles)
def plot_with_styles(x, y):
    plt.figure()  # إنشاء شكل جديد
    plt.plot(x, y, linestyle='--', color='blue', linewidth=2, marker='o', markersize=5)  # تخصيص نمط الخط
    plt.title("Styled Plot Example")  # عنوان الرسم
    plt.xlabel("X-axis")  # تسمية المحور الأفقي
    plt.ylabel("Y-axis")  # تسمية المحور الرأسي
    plt.grid(True)  # تفعيل الشبكة
    plt.show()  # عرض الرسم

# الدالة الرابعة: إضافة نصوص وأسهم على الرسم (Annotations)
def annotated_plot():
    x = np.linspace(0, 10, 100)  # إنشاء قيم x متدرجة
    y = np.sin(x)  # حساب القيم المقابلة لـ y

    plt.figure(figsize=(10, 6))  # إنشاء شكل جديد
    plt.plot(x, y, label="Sine Wave", color="green")  # رسم الموجة
    plt.annotate('Maximum', xy=(np.pi / 2, 1), xytext=(2, 1.5),
                 arrowprops=dict(facecolor='black', arrowstyle="->"))  # إضافة سهم عند القمة
    plt.title("Annotated Plot Example")  # عنوان الرسم
    plt.xlabel("X-axis")  # تسمية المحور الأفقي
    plt.ylabel("Y-axis")  # تسمية المحور الرأسي
    plt.legend()  # إضافة مفتاح
    plt.grid(True)  # تفعيل الشبكة
    plt.show()  # عرض الرسم

# الدالة الخامسة: رسم مساحة تحت المنحنى (Filled Area)
def filled_area_plot(x, y):
    plt.figure(figsize=(8, 6))  # إنشاء شكل جديد
    plt.fill_between(x, y, color='skyblue', alpha=0.4)  # تعبئة المنطقة تحت المنحنى
    plt.plot(x, y, color='blue', linewidth=2)  # رسم الخط فوق المنطقة
    plt.title("Filled Area Example")  # عنوان الرسم
    plt.xlabel("X-axis")  # تسمية المحور الأفقي
    plt.ylabel("Y-axis")  # تسمية المحور الرأسي
    plt.show()  # عرض الرسم

# أمثلة على استخدام كل دالة:

# 1. رسم عدة رسوم في نفس الشكل
multiple_subplots()

# 2. رسم هيستوجرام
data = np.random.normal(0, 1, 1000)  # توليد بيانات عشوائية
histogram_example(data)

# 3. رسم بيانات بخطوط متنوعة
x = np.linspace(0, 10, 50)  # قيم x
y = np.sin(x)  # قيم y
plot_with_styles(x, y)

# 4. رسم مع إضافة نصوص وأسهم
annotated_plot()

# 5. رسم منطقة مملوءة تحت منحنى
filled_area_plot(x, y)

# المكتبات التي يجب تثبيتها:
# pip install matplotlib numpy




# https://chatgpt.com/share/674e0e31-5c64-800a-8d21-e2aa0c44e3c3