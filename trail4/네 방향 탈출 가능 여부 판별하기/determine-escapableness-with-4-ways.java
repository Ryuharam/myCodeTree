import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();
        // Please write your code here.

        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];

        q.add(new int[]{0,0});
        visited[0][0] = true;

        while(!q.isEmpty()){
            int[] cur = q.poll();

            for(int d=0 ; d<4 ; d++){
                int nr = cur[0] + dr[d];
                int nc = cur[1] + dc[d];

                if(0<=nr && nr<n && 0<=nc && nc<m && !visited[nr][nc] && grid[nr][nc] == 1){
                    if(nr == n-1 && nc == m-1){
                        System.out.println(1);
                        return;
                    }

                    q.add(new int[]{nr,nc});
                    visited[nr][nc] = true;
                }
            }
        }

        System.out.println(0);
    }
}