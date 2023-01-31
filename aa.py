import src.textflowsms as tf

tf.useKey("a8c9H5AMVqeiW6lUHNYia4yb9RZObMyUmWDI2GJeaol9R177Ng45F4yfOg4856w")

result = tf.sendSMS("+381611231234", "Dummy message text...")
print(result)