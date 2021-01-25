public class Person {
    private String name;
    private int age;
    private int cashAmount;
    private BankAccount account;

    public void setAge(int newAge) {
        if (newAge >= 0) {
            age = newAge;
        }
    }

    public int getAge() {
        return age;
    }

    public void setName(String newName) {
        name = newName;
    }

    public String getName() {
        return name;
    }

    public void setCashAmount(int newCashAmount) {
        if(newCashAmount >= 0) {
            cashAmount = newCashAmount;
        }
    }

    public int getCashAmount() {
        return cashAmount;
    }

    public void setAccount(BankAccount newAccount) {
        account = newAccount;
    }

    public BankAccount getAccount() {
        return account;
    }

    public boolean transfer(Person to, int amount) {
        if (amount >= 0 || amount > account.getBalance()) {
            account.setBalance(getAccount().getBalance() - amount);
            to.getAccount().setBalance(to.getAccount().getBalance() + amount);
            System.out.println("true - from: [" + getAccount().getOwner().getName() + "], to: [" + to.getName() + "], amount: ["
                    + amount + "], balance: [" + to.getAccount().getBalance() + "]");
            return true;
        } else {
            System.out.println("false - from: [" + getAccount().getOwner().getName() + "], to: [" + to.getName() + "], amount: ["
                    + amount + "], balance: [" + to.getAccount().getBalance() + "]");
            return false;
        }
    }

    public boolean transfer(BankAccount to, int amount) {
        if (amount >= 0 || amount > account.getBalance()) {
            account.setBalance(getAccount().getBalance() - amount);
            to.setBalance(to.getBalance() + amount);
            System.out.println("true - from: [" + getAccount().getOwner().getName() + "], to: [" + to.getOwner().getName() + "], amount: ["
                    + amount + "], balance: [" + account.getBalance() + "]");
            return true;
        } else {
            System.out.println("false - from: [" + getAccount().getOwner().getName() + "], to: [" + to.getOwner().getName() + "], amount: ["
                    + amount + "], balance: [" + account.getBalance() + "]");
            return false;
        }
    }
}
