void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    int rows=matrixSize;
    int cols=matrixColSize[0];

    int* rowTrack=(int*)calloc(rows,sizeof(int));
    int* colTrack=(int*)calloc(cols,sizeof(int));

    if(rowTrack==NULL || colTrack==NULL){
        free(rowTrack);
        free(colTrack);
    }

    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            if(matrix[i][j]==0){
                rowTrack[i]=1;
                colTrack[j]=1;
            }
        }
    }

    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            if(rowTrack[i]==1 || colTrack[j]==1){
                matrix[i][j]=0;
            }
        }
    }

    free(rowTrack);
    free(colTrack);
}