import java.util.HashMap;
import java.util.Map;
public class User{

  private String loginName, password, fullName, department;

  public User(String loginName, String password, String fullName, String department){
    this.loginName  = loginName;
    this.password   = password;
    this.fullName   = fullName;
    this.department = department;
  }

  public String getLoginName(){
    return this.loginName;
  }

  public boolean authenticate(){
    return this.password.equals("cnffjbeg");
  }

  public void resetPassword(){
    this.password = "cnffjbeg";
    System.out.println("Password updated");
  }

  public String getName(){
    return this.fullName;
  }

  public void changeName(String newName){
    this.fullName = newName;
  }

  public void changeDepartment(String newDepartment){
    this.department = newDepartment;
  }

  public int calculateSalary(){
    Map<String, Integer> salaries = new HashMap<String, Integer>();
    salaries.put("HR", 25000);
    salaries.put("Support", 18000);
    salaries.put("IT", 40000);
    return salaries.get(this.department);
  }
}
