int n = 0;
        n = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero al cual desea ver el factrial"));
        int ac = 1;
        while(n >= 1){
            ac = ac*n;
            n = n-1;
        }
        JOptionPane.showMessageDialog(null, ac);
        