import { Entity, PrimaryColumn, Column } from "typeorm";

@Entity('Log')
export class Log {

    @PrimaryColumn()
    Date: string;

    @Column()
    Msg: string;
    
}