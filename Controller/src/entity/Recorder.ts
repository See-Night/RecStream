import { Entity, Column, PrimaryColumn } from "typeorm";

@Entity('Recorder')
export class Recorder {

    @PrimaryColumn()
    PID: string;

    @Column()
    Status: string;

    @Column()
    LiveURL: string;

}
