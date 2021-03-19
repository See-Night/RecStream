import {Entity, Column, PrimaryColumn} from "typeorm";

@Entity('User_user')
export class User {

    @PrimaryColumn()
    username: string;

    @Column()
    password: string;

    @Column({ nullable: true })
    UUID: string;

}
