<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" media="screen" title="no title" charset="utf-8">
  <style media="screen">
    .row {
      margin-top: 200px;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col-sm-offset-4 col-sm-4">
        <?php
          if(isset($_POST['username']) && $_POST['username'] == 'james' && isset($_POST['password']) && $_POST['password'] == 'password'){
            ?>
            <div class="alert alert-success">
              You have signed in successfully
            </div>
            <p>
              Some more interesting stuff...
            </p>

        <?php } else{ ?>
        <form class="form" method="post" action="login.php">
          <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" class="form-control" name="username">
          </div>
          <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" class="form-control" name="password">
          </div>
          <input type="submit" value="Login" class="btn btn-primary btn-block">
        </form>
        <?php }?>
      </div>
    </div>
  </div>
</body>
</html>
