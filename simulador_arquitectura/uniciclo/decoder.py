class Decoder:
    def __init__(self, Op):
        if Op == '0000011':
            self.RegWrite = '1'
            self.ImmSrc = '00'
            self.ALUSrc = '1'
            self.MemWrite = '0'
            self.ResultSrc = '1'
            self.Branch = '0'
            self.ALUOp = '00'
        elif Op == '0100011':
            self.RegWrite = '0'
            self.ImmSrc = '01'
            self.ALUSrc = '1'
            self.MemWrite = '1'
            self.ResultSrc = 'x'
            self.Branch = '0'
            self.ALUOp = '00'
        elif Op == '0010011':
            self.RegWrite = '1'
            self.ImmSrc = 'xx'
            self.ALUSrc = '0'
            self.MemWrite = '0'
            self.ResultSrc = '0'
            self.Branch = '0'
            self.ALUOp = '10'
        elif Op == '0110011':
            self.RegWrite = '1'
            self.ImmSrc = 'xx'
            self.ALUSrc = '0'
            self.MemWrite = '0'
            self.ResultSrc = '0'
            self.Branch = '0'
            self.ALUOp = '10'
        elif Op == '1100011':
            self.RegWrite = '0'
            self.ImmSrc = '10'
            self.ALUSrc = '0'
            self.MemWrite = '0'
            self.ResultSrc = 'x'
            self.Branch = '1'
            self.ALUOp = '01'

    def decode(self, Op, Funct, Rd):
        # Main Decoder
        if Op == 0b00:
            if Funct[5]:
                self.controls = 0b0000101001
            else:
                self.controls = 0b0000001001
        elif Op == 0b01:
            if Funct[0]:
                self.controls = 0b0001111000
            else:
                self.controls = 0b1001110100
        elif Op == 0b10:
            self.controls = 0b0110100010
        else:
            self.controls = None

        # ALU Decoder
        if self.ALUOp:
            # which DP Instr?
            case = Funct[4:1]
            if case == 0b0100:
                self.ALUControl = 0b00  # ADD
            elif case == 0b0010:
                self.ALUControl = 0b01  # SUB
            elif case == 0b0000:
                self.ALUControl = 0b10  # AND
            elif case == 0b1100:
                self.ALUControl = 0b11  # ORR
            else:
                self.ALUControl = None

            # update flags if S bit is set (C & V only for arith)
            self.FlagW[1] = Funct[0]
            self.FlagW[0] = Funct[0] and (self.ALUControl == 0b00 or self.ALUControl == 0b01)
        else:
            self.ALUControl = 0b00  # add for non-DP instructions
            self.FlagW = [0b00]  # don't update Flags

        # PC Logic
        self.PCS = (Rd == 0b1111 and RegW) or self.Branch

# Uso del decodificador
Op = 0b00
Funct = 0b110110
Rd = 0b0101
decoder_instance = Decoder(Op, Funct, Rd)