public class ObjectExample{
  public static void main(String[] args){
    User employee1;
    String[] itSkills = {"Windows", "Linux", "MS Exchange", "FTP"}; 
    ITUser it_user1;
    employee1 = new User("jbubb", "cnffjbeg", "James Bubb", "IT");
    it_user1 = new ITUser("djones", "cnffjbeg", "Dave Jones", "Support", itSkills);
    System.out.println(employee1.calculateSalary());
    System.out.println(it_user1.getName());
    it_user1.listSkills();
  }
}
