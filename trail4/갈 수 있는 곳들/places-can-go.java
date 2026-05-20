import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {

    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int[][] grid = new int[n][n];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();

        int[][] starts = new int[k][2];
        boolean[][] visited = new boolean[n][n];
        Queue<int[]> q = new LinkedList<>();
        int cnt = 0;
    
        for (int i = 0; i < k; i++) {
            starts[i][0] = sc.nextInt() - 1;
            starts[i][1] = sc.nextInt() - 1;
            visited[starts[i][0]][starts[i][1]] = true;
            q.add(new int[]{starts[i][0], starts[i][1]});
            cnt++;
        }

        // Please write your code here.
        while(!q.isEmpty()){
            int[] cur = q.poll();


            for(int d=0 ; d<4 ; d++){
                int nr = cur[0] + dr[d];
                int nc = cur[1] + dc[d];

                if(0<=nr && nr<n && 0<=nc && nc<n && !visited[nr][nc] && grid[nr][nc] == 0){
                    cnt++;
                    visited[nr][nc] = true;
                    q.add(new int[]{nr,nc});
                }
            }
        }

        System.out.println(cnt);

    }
}