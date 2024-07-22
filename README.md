# Scientific-Calculator-using-PyTQ6-GUI-Application

**OBJECTIVE:**

         The scientific calculator implemented using PyQt6 showcases the integration of a graphical user interface (GUI)
         with functional calculations. Here’s a concise summary of the key aspects covered:

**GUI Design:**

The calculator’s GUI was designed using PyQt6, a Python library for creating desktop applications with Qt. The main window (QMainWindow) was utilized to house the calculator interface, with a central widget (QWidget) managing the layout.

**Components:**

1.Display (QLineEdit): A QLineEdit widget was employed for both displaying input and output. It featured read-only properties to prevent direct user input, maintaining control over the 
                       displayed content.
                       
2.Buttons (QPushButton): Functional buttons for numerical digits, basic arithmetic operators (+, -, *, /), and scientific functions (trigonometric functions, logarithm, square root) were 
                        incorporated.Each button was dynamically connected to methods handling user interactions, ensuring responsive behavior upon clicking.
                        
**Functionality:**

1.Basic Arithmetic Operations:
          The calculator supported fundamental arithmetic operations (addition, subtraction, multiplication, division) using Python’s eval() function for evaluation.
          
2.Scientific Functions:
          Implemented trigonometric functions (sin, cos, tan), logarithm (log), square root (sqrt), and constants (pi, e), utilizing Python's math module for accurate computations.
          
3.Error Handling:
          Robust error handling mechanisms were implemented to manage exceptions gracefully, ensuring user-friendly error messages for invalid inputs or mathematical operations.
          
4.Styling and Customization:
    # Stylesheets:
          Qt stylesheets were applied to customize the appearance of widgets. This included setting background colors (background-color) for the main window, buttons, and the 
          input/output display (QLineEdit).
          
**Conclusion:**
        The implementation demonstrated effective utilization of PyQt6 for developing a functional and visually appealing scientific calculator application. By leveraging PyQt6’s capabilities, the project achieved seamless integration of GUI elements with powerful mathematical functionalities. Future enhancements could include additional scientific functions, improved user interface elements, and support for more advanced mathematical operations.
        
        Overall, the PyQt6-based scientific calculator project exemplifies the synergy between Python programming and GUI development,
        showcasing practical application in educational, scientific, and professional contexts.
