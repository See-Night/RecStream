import { Entity, Column, PrimaryColumn } from "typeorm";

@Entity('SystemStatus')
export class SystemStatus {

    @PrimaryColumn()
    status: number;

    @Column()
    description: string;
    
}
