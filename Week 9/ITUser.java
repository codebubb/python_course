public class ITUser extends User{
  private String[] skills;
  public ITUser(String loginName, String password, String fullName, String department, String[] skills){
    super(loginName, password, fullName, department);
    this.skills = skills;
  }
  public void listSkills(){
    System.out.println("Skills:");
    for(int i=0; i < skills.length; i++){
      System.out.println(this.skills[i]);
    }
  }

  public void fixThings(){
    System.out.println("I'm here because you broke something!");
  }
}
