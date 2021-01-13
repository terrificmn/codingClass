<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact form</title>
</head>
<body>
  <main>
    <p>Send E-mail</p>
    <form action="37_contactform.php" method="POST">
      <input type="text" name="name" placeholder="Full name">
      <input type="text" name="mail" placeholder="Your e-mail">
      <input type="text" name="subject" placeholder="Subject">
      <textarea name="message" placeholder="Message"></textarea>
      <button type="submit" name="submit">SEND E-MAIL</button>
    </form>
  </main>
</body>
</html>