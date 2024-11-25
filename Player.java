public class Player {

  String name;
  int score;
  boolean isStanding;

  public Player(String name){
    this.name = name;
    this.score = 0;
    this.isStanding = false;
  }

  public String getName(){
    return this.name;
  }

  public int getScore(){
    return this.score;
  }

  public void addScore(int points){
    this.score += points;
  }

  public boolean isStanding(){
    if (this.isStanding){
      return true;
    }
    else {
      return false;
    }

  }

  public void stand(){
    this.isStanding = true;    
  }

  public static void main(String args[]){
  }


}
